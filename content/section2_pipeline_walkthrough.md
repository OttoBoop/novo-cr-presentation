# Seção 2: Pipeline de Correção — Texto para Slides

## Slide 2.0: Introdução ao Pipeline

**Como a IA processa uma prova?**

O NOVO CR transforma documentos brutos em análise pedagógica através de um pipeline automatizado de 6+ etapas. Cada etapa gera um documento que o professor pode visualizar, editar e revisar antes de prosseguir.

*[Inserir: screenshot 04_pipeline_diagram.png]*

---

## Slide 2.1: Etapa 1 — Extração de Questões 🔎

**A IA lê o enunciado e identifica cada questão.**

- Classifica cada questão pelo tipo de raciocínio exigido
- Identifica habilidades cognitivas testadas (5 categorias: recuperação, compreensão, aplicação, análise, síntese)
- Gera um JSON estruturado com número, enunciado, itens e pontuação máxima

> O professor recebe um mapa completo da prova antes de qualquer correção.

---

## Slide 2.2: Etapa 2 — Extração de Gabarito 🧩

**Estrutura as respostas corretas.**

- A IA organiza as respostas esperadas por questão
- Associa critérios de pontuação a cada item
- Identifica respostas alternativas válidas

---

## Slide 2.3: Etapa 3 — Extração de Respostas 📝

**Lê o que o aluno escreveu.**

- Processa a prova respondida do aluno
- Identifica cada resposta por questão
- Lida com caligrafia, formatos variados e respostas parciais

---

## Slide 2.4: Etapa 4 — Correção ✅

**Compara com gabarito e atribui notas — mas vai muito além.**

Não é um simples "certo ou errado". Para cada questão, a correção narrativa inclui:

- **Nota** com justificativa
- **Análise do raciocínio** — o que o aluno estava pensando
- **Tipo de erro** — conceitual, de execução, de interpretação
- **Potencial demonstrado** — o que o aluno quase acertou

*[Inserir: trecho do relatório de correção PDF]*

> *"Como professor, quero que a correção inclua uma análise narrativa do que o aluno estava pensando, o tipo de erro cometido, e o potencial demonstrado — não só a nota."*

---

## Slide 2.5: Etapa 5 — Análise de Habilidades 📊

**Identifica pontos fortes e fracos do aluno.**

- Perfil de habilidades demonstradas vs. esperadas
- Consistência de erros entre questões
- Síntese pedagógica: o que o aluno sabe fazer bem, onde precisa melhorar
- Linguagem construtiva, pensada para eventual acesso direto pelo aluno

---

## Slide 2.6: Etapa 6 — Relatório Final 📄

**Narrativa holística: olha o todo primeiro, depois os detalhes.**

O relatório final combina nota, habilidades e análise narrativa numa leitura fluida. Estrutura:

1. Visão geral do desempenho
2. Análise detalhada por questão
3. Pontos fortes e áreas de melhoria
4. Recomendações específicas para o aluno

> *"Um relatório que posso mostrar ao aluno e aos pais."*

---

## Slide 2.7: Etapas 7-9 — Relatórios de Desempenho (Novo!)

**De uma prova para o currículo inteiro — três níveis de análise agregada:**

### 📋 Desempenho por Tarefa (Atividade)
- Como a turma se saiu nesta prova específica
- Padrões de acerto/erro por questão
- Exemplos específicos de alunos

### 👥 Desempenho por Turma
- Evolução ao longo do semestre
- Erros persistentes
- Perfil coletivo de aprendizagem

### 📚 Desempenho por Matéria
- Comparação entre turmas
- Eficácia do currículo
- O que deve mudar no ensino

> *"A matéria está sendo ensinada bem? O que deveria mudar no currículo?"*

---

## Slide 2.8: Cada Etapa Gera um Documento

**Transparência total: o professor vê e controla cada passo.**

- Documentos em JSON (dados estruturados) + PDF (narrativa legível)
- Tudo editável — o professor pode sobrescrever qualquer resultado
- Histórico completo: sabe qual IA processou cada documento
- Múltiplos provedores: OpenAI, Anthropic, Google, modelos locais
