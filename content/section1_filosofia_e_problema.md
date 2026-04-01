# Seção 1: Problema e Filosofia — Texto para Slides

## Slide 1.0: Título
**NOVO CR**
*Mais que um Número*

---

## Slide 1.1: O Problema

**O que acontece hoje na correção de provas?**

- Professores corrigem dezenas de provas entre uma aula e outra
- Feedback para o aluno se resume a uma nota numérica
- Não há tempo para analisar padrões de aprendizado da turma
- Ferramentas de correção automática substituem o professor — ou entregam checklists genéricos

> O professor precisa de **tempo**, não de mais uma ferramenta que ele precisa aprender a usar.

---

## Slide 1.2: A Nossa Resposta — "Potencializar, Não Substituir"

**NOVO CR potencializa a correção do professor — não substitui o professor.**

- A IA assiste o professor. Ela **nunca** toma decisões finais.
- O professor pode **sempre** revisar, modificar e sobrescrever qualquer resultado da IA.
- O sistema foi desenhado para que o professor **não precise aprender IA** — ele só precisa dos resultados.

> *"A IA assiste professores — ela não toma decisões finais. Professores sempre podem sobrescrever."*

---

## Slide 1.3: "Mais que um Número"

**Alunos são mais que seu CR (Coeficiente de Rendimento).**

- O nome "NOVO CR" fala a linguagem das universidades — administradores e coordenadores pensam em termos de CR
- Mas o sistema entrega muito mais que uma nota: entrega **narrativas pedagógicas**
- Cada relatório conta a história do raciocínio do aluno, seus erros, seu potencial

> *"Reforça que alunos são mais do que sua nota/CR."*

---

## Slide 1.4: Narrativa Pedagógica, Não Checklists

**O output de checklist violava todos os princípios originais. Este redesenho restaura a visão original.**

Antes:
- ✗ Checklist superficial: "acertou / errou / parcial"
- ✗ Sem análise do raciocínio do aluno
- ✗ Notas já fazem isso — o relatório deveria contar a **história** da aprendizagem

Agora — arquitetura narrativa em 3 níveis:
1. **Microscópio por questão** — o que o aluno estava pensando, tipo de erro, potencial demonstrado
2. **Síntese de padrões** — perfil de habilidades, consistência de erros
3. **Narrativa holística** — olha o todo primeiro, depois os detalhes, combina notas + habilidades

> *"Notas já lidam com números; este relatório deveria contar a história da aprendizagem da turma."*

---

## Slide 1.5: Confiança Através da Transparência

**Mostre o que a IA fez, por quê, e deixe o professor sobrescrever. Nunca uma caixa preta.**

- Cada etapa do pipeline gera um documento visível e editável
- O professor vê exatamente o que a IA produziu em cada passo
- A qualidade da IA é explicitamente verificada por humanos antes de ser liberada
- Resultados que o professor pode **confiar e defender para os alunos**

---

## Slide 1.6: Feedback Acima de Notas

**Cada decisão de design responde a estas perguntas:**

1. Isso dá aos alunos **mais feedback**?
2. Isso permite relatórios **mais abrangentes**?
3. Isso ajuda professores a **entender o progresso** dos alunos?
4. Isso torna a correção **mais eficiente sem sacrificar qualidade**?

> *"Resultados que eles podem confiar e defender para os alunos."*

---

## Slide 1.7: Revelação Progressiva

**Um professor corrigindo 30 provas não deveria ter que configurar parâmetros de IA.**

- Mostre o essencial primeiro, revele complexidade sob demanda
- O sistema é autoexplicativo — tooltips e orientações em cada elemento
- Funcionalidades avançadas existem mas ficam escondidas até o professor querer usá-las
- Primeiro uso: **zero configuração**

---

## Slide 1.8: Análise em Múltiplos Níveis

**De uma questão até o currículo inteiro:**

| Nível | O que analisa | Para quem |
|-------|--------------|-----------|
| **Questão** | Raciocínio do aluno naquela questão específica | Professor |
| **Aluno** | Perfil completo: notas, habilidades, evolução | Professor + Aluno |
| **Atividade** | Como a turma se saiu nesta prova | Professor |
| **Turma** | Evolução ao longo do tempo, erros persistentes | Coordenador |
| **Matéria** | Comparação entre turmas, eficácia do currículo | Coordenador |

> *"A matéria está sendo ensinada bem? O que deveria mudar no currículo?"*

---

## Slide 1.9: Flexibilidade Multi-Provedor

**Sem dependência de um único provedor de IA.**

- OpenAI (GPT-5, o3)
- Anthropic (Claude Opus, Sonnet, Haiku)
- Google (Gemini 3 Flash/Pro)
- Ollama (modelos locais)

> *"Framework para experimentação com diferentes IAs na correção automatizada."*

O professor não escolhe o modelo — o sistema escolhe o melhor para cada tarefa. Mas pesquisadores podem comparar resultados entre provedores.
