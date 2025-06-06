# 🔥 Detector de Fadiga Térmica – Visão Computacional com Python + MediaPipe

## 🧠 Descrição do Problema

O Brasil está enfrentando uma escalada crítica nas temperaturas médias, com aumentos de até **3°C** em algumas regiões. O **aquecimento global** intensifica as **ondas de calor**, que se tornam mais frequentes e duradouras, colocando em risco especialmente os **idosos, pessoas isoladas, trabalhadores em ambientes fechados** e populações vulneráveis.

Entre 2000 e 2018, mais de **48 mil mortes no Brasil** foram atribuídas às ondas de calor. Durante apagões ou em locais sem ventilação adequada, o **mal súbito por calor extremo pode ocorrer de forma silenciosa**, sem chances de socorro imediato.

---

## 🤖 Visão Geral da Solução

Diante do avanço das mudanças climáticas, propomos uma solução baseada em **visão computacional** capaz de **detectar sinais precoces de exaustão térmica** em tempo real, utilizando apenas uma **webcam comum, Python e MediaPipe**.

A proposta visa reduzir riscos de mal súbito por calor extremo, especialmente em situações de **apagão, isolamento ou ambientes mal ventilados**, onde não há supervisão constante.

### 🧩 Funcionalidades principais:

- ✅ Monitoramento contínuo de **gestos e posturas corporais**
- ✅ Detecção de sinais como: cabeça abaixada, postura curvada, mãos no rosto e imobilidade
- ✅ Geração de alerta automático quando padrões de risco são identificados
- ✅ Alerta para ausência de pessoas no ambiente por tempo prolongado
- ✅ Detecção de possível corpo deitado (queda)
- ✅ Interface leve e executável localmente, sem necessidade de internet após instalação

---

### 🛠️ Como Funciona na Prática

1. O usuário posiciona-se em frente à câmera;
2. O sistema inicia o rastreamento de pontos do corpo e rosto via MediaPipe;
3. Ao detectar indícios de fadiga térmica, um **alerta visual é exibido na tela**, simulando uma notificação de emergência;
4. Esse alerta pode ser facilmente adaptado para integração com **sistemas de automação**, notificações ou alarmes físicos em versões futuras.

---

## 🎯 Atividades Detectadas Pelo Sistema

O sistema detecta e emite alertas para os seguintes comportamentos relacionados à fadiga térmica. Para testá-lo, posicione-se em frente à webcam e simule as seguintes situações:

- 🧍‍♂️ **Cabeça levemente abaixada**  
  → Incline a cabeça para frente (simulando cansaço ou sono leve).

- ✋ **Mão no rosto**  
  → Encoste a mão próxima aos olhos ou bochechas (simulando exaustão ou desconforto).

- 🪑 **Postura curvada**  
  → Sente-se de forma desleixada, com ombros caídos (indicando relaxamento excessivo ou fadiga).

- 🧊 **Imobilidade total por mais de 7 segundos**  
  → Fique completamente imóvel para simular um possível desmaio.

- 🛌 **Corpo deitado**  
  → Deite-se no chão ou tente ficar com o corpo inteiro horizontalizado no quadro.

- 🚫 **Ausência no quadro**  
  → Saia de frente da câmera por mais de 7 segundos para simular uma queda ou abandono de posição.

> ⚠️ Após cada simulação, observe os alertas visuais que aparecem na tela.  
> O sistema foi projetado para ser sensível, mas não invasivo – alertas desaparecem após o retorno ao estado normal.

---

## ⚠️ Limitações Conhecidas

Embora o sistema funcione de forma eficiente para a detecção de sinais básicos de fadiga térmica, ainda existem limitações técnicas importantes a considerar:

- **Monitora apenas uma pessoa por vez**  
  A detecção é baseada em um único esqueleto corporal (pose), não sendo compatível com múltiplos usuários simultaneamente.

- **Pode gerar falsos positivos em situações ambíguas**  
  Como, por exemplo, uma pessoa parada olhando para o lado ou com gestos incomuns que não representem fadiga real.

- **Não realiza análise emocional avançada**  
  O sistema não detecta expressões faciais complexas como tristeza, angústia ou estresse – apenas sinais físicos como postura, cabeça inclinada e imobilidade.

Esses pontos servem como base para evoluções futuras e integração com tecnologias mais avançadas.

---

## 🎥 Vídeo Demonstrativo

📽️ Assista ao funcionamento da solução na prática:  
➡️ [Clique aqui para assistir]([https://youtu.be/SEU-LINK-AQUI](https://www.youtube.com/watch?v=m4sUIODWykk))

---

### 🧪 Requisitos Básicos

- Uma webcam funcional (embutida ou externa)
- Python 3.10 instalado
- Sistema operacional Windows, Linux ou macOS
- Conexão com a internet apenas durante a instalação das dependências

---

## 🧠 Tecnologias Utilizadas

- Python 3.10
- MediaPipe

---

## 🧪 Instruções para Execução

```bash
# 1. Clone o repositório
git clone https://github.com/Torugo0/Soltrix_IOT

# 2. Acesse a pasta
cd SOLTRIX_IOT

# 3. Instale as dependências necessárias (Verifique se sua versão do python é igual a 3.10 ou inferior para uso do mediapipe)
pip install mediapipe opencv-python

```
---

## 📚 Fontes Utilizadas

- **Brasil tem aumento de até 3°C na temperatura de algumas regiões**  
  Agência Brasil – [https://agenciabrasil.ebc.com.br/meio-ambiente/noticia/2024-11/brasil-tem-aumento-de-ate-3oc-na-temperatura-de-algumas-regioes](https://agenciabrasil.ebc.com.br/meio-ambiente/noticia/2024-11/brasil-tem-aumento-de-ate-3oc-na-temperatura-de-algumas-regioes)

- **Verão 2024/2025 foi o sexto mais quente no Brasil desde 1961**  
  INMET – [https://portal.inmet.gov.br/noticias/ver%C3%A3o-2024-2025-foi-o-sexto-mais-quente-no-brasil-desde-1961](https://portal.inmet.gov.br/noticias/ver%C3%A3o-2024-2025-foi-o-sexto-mais-quente-no-brasil-desde-1961)

- **Aquecimento global amplifica ondas de calor que podem assolar cidades brasileiras até 15 vezes ao ano**  
  Pesquisa FAPESP – [https://revistapesquisa.fapesp.br/aquecimento-global-amplifica-ondas-de-calor-que-podem-assolar-cidades-brasileiras-ate-15-vezes-ao-ano](https://revistapesquisa.fapesp.br/aquecimento-global-amplifica-ondas-de-calor-que-podem-assolar-cidades-brasileiras-ate-15-vezes-ao-ano)

- **Brasil teve a temperatura global média 1,59°C acima do nível pré-industrial em 2024**  
  CNN Brasil – [https://www.cnnbrasil.com.br/nacional/brasil/verao-de-2025-e-segundo-mais-quente-da-historia](https://www.cnnbrasil.com.br/nacional/brasil/verao-de-2025-e-segundo-mais-quente-da-historia)

- **Mais de 48 mil pessoas morreram por ondas de calor no Brasil entre 2000 e 2018**  
  Observatório do Clima – [https://www.oc.eco.br/mais-de-48-mil-pessoas-morreram-por-ondas-de-calor-no-brasil-entre-2000-e-2018](https://www.oc.eco.br/mais-de-48-mil-pessoas-morreram-por-ondas-de-calor-no-brasil-entre-2000-e-2018)

- **São Paulo registra cinco mortes e aumento de 102% nos atendimentos por efeitos do calor em 2023**  
  CNN Brasil – [https://www.cnnbrasil.com.br/nacional/sao-paulo-registra-cinco-mortes-e-aumento-de-102-nos-atendimentos-por-efeitos-do-calor-em-2023-2](https://www.cnnbrasil.com.br/nacional/sao-paulo-registra-cinco-mortes-e-aumento-de-102-nos-atendimentos-por-efeitos-do-calor-em-2023-2)

- **Calor extremo aumenta mortalidade no Rio de Janeiro, diz pesquisa**  
  CNN Brasil – [https://www.cnnbrasil.com.br/nacional/sudeste/rj/calor-extremo-aumenta-mortalidade-no-rio-de-janeiro-diz-pesquisa](https://www.cnnbrasil.com.br/nacional/sudeste/rj/calor-extremo-aumenta-mortalidade-no-rio-de-janeiro-diz-pesquisa)

---

## 👥 Integrantes

| Nome                                | RM         |
|-------------------------------------|------------|
| Vitor Hugo Rodrigues                | RM: 97758  |
| Leticia Resina                      | RM: 98069  |
| Gabriel Machado                     | RM: 99880  |
