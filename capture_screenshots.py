"""Capture screenshots from NOVO CR live site for presentation.
Run: pip install playwright && playwright install chromium && python capture_screenshots.py
"""
import asyncio
from pathlib import Path
from playwright.async_api import async_playwright

SCREENSHOTS_DIR = Path(__file__).parent / "screenshots"
SCREENSHOTS_DIR.mkdir(exist_ok=True)

BASE_URL = "https://ia-educacao-v2.onrender.com"

CAPTURES = [
    ("01_dashboard.png", f"{BASE_URL}", "Dashboard / home page"),
    ("02_materia_turma.png", f"{BASE_URL}/#materia=f95445ace30e7dc5&turma=6b5dc44c08aaf375", "Matéria > Turma view"),
    ("03_atividade.png", f"{BASE_URL}/#materia=f95445ace30e7dc5&turma=6b5dc44c08aaf375&atividade=effad48d128c7083", "Atividade view with documents"),
]

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page(viewport={"width": 1440, "height": 900})

        for filename, url, desc in CAPTURES:
            print(f"Capturing: {desc}")
            await page.goto(url, wait_until="networkidle", timeout=30000)
            await asyncio.sleep(2)  # Let animations settle
            path = SCREENSHOTS_DIR / filename
            await page.screenshot(path=str(path), full_page=False)
            print(f"  Saved: {path}")

        # Also capture the pipeline diagram
        diagram_path = Path(__file__).parent.parent / "IA_Educacao_V2" / "frontend" / "diagram_pipeline.html"
        if diagram_path.exists():
            print("Capturing: Pipeline diagram")
            await page.goto(f"file:///{diagram_path.resolve()}", wait_until="load")
            await asyncio.sleep(1)
            path = SCREENSHOTS_DIR / "04_pipeline_diagram.png"
            await page.screenshot(path=str(path), full_page=False)
            print(f"  Saved: {path}")

        await browser.close()
    print(f"\nDone! {len(list(SCREENSHOTS_DIR.glob('*.png')))} screenshots saved to {SCREENSHOTS_DIR}")

if __name__ == "__main__":
    asyncio.run(main())
