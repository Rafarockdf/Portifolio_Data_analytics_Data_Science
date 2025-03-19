
# Predição de Vendas para Melhores Compras

## Introdução
Este projeto tem como objetivo predizer o volume de vendas semanais para o E-Commerce Melhores Compras. A partir da análise de dados históricos e da aplicação de algoritmos de aprendizado de máquina, busca-se identificar o modelo capaz de gerar previsões mais acuradas, contribuindo para a geração de insights financeiros importantes.

## Limpeza de Dados

### Descrição das Variáveis
- **Date**: Data em que a observação foi feita.
- **Weekly_Sales**: Vendas da empresa na semana, indicada pelo campo Date.
- **Holiday_Flag**: Indica se houve um feriado na semana medida.
- **Temperature**: Temperatura média registrada naquela semana.
- **Fuel_Price**: Preço do combustível (deve ser dividido por 1.000 para se obter o preço em reais e centavos).
- **CPI**: Índice que indica o nível de atividade econômica da região.
- **Unemployment**: Nível de desemprego medido nacionalmente (deve ser dividido por 1.000 para se obter a informação em percentual).

### Pré-Processamento
- Não houve dados duplicados na base.
- Não houve valores negativos ou nulos.
- **Fuel_Price**: Dados divididos por 1000 para adequação.
- **Unemployment**: Dados divididos por 1000 para adequação.
- **Date**: Transformação para o tipo datetime do pandas, garantindo o formato DD/MM/YYYY.

## Análise Exploratória de Dados (AED)

### Visualização dos Dados

#### Gráfico de Linha: Comparação das Vendas ao Longo do Tempo
Observou-se um aumento significativo no volume de vendas durante o final de ano, além de flutuações constantes em outros períodos.

#### Gráfico de Linha: Linhas de Tendência Vendas ao Longo do Tempo
As vendas semanais apresentam uma tendência de crescimento ao longo do tempo, sugerindo uma correlação positiva entre as semanas e as vendas.

#### Análise de Correlação com Gráficos de Dispersão
Não foram encontradas correlações fortes entre a variável Weekly_Sales e as variáveis independentes.

#### Visualização da Correlação entre Variáveis na Tabela Sales (Mapa de Calor)
As variáveis Date, Holiday_Flag, Fuel_Price e CPI apresentam as maiores correlações com a variável de interesse (Weekly_Sales).

## Modelagem - Aprendizado de Máquina

### Técnicas/Algoritmos de Regressão
- **Gradient Boosting (XGBoost)**: Alto desempenho e precisão, corrige erros de modelos anteriores.
- **SVM (Support Vector Machine)**: Corrige erros de modelos anteriores, rápido e eficaz.
- **Random Forest**: Baseado em várias árvores de decisão, robusto e menos propenso ao overfitting.
- **Linear Regression**: Ajusta uma linha reta para representar a relação entre variáveis.

### Processamento
- **Divisão dos dados**: 80% para treinamento e 20% para testes.

## Análise dos Resultados: Testando a Performance de 4 Modelos

- **XGBRegressor**: Melhor desempenho, menor MSE e RMSE, R² de 66%.
- **Random ForestRegressor**: Bom desempenho, R² de 41%.
- **Linear Regression**: Desempenho mais fraco, R² de 2%.
- **SVR**: Pior desempenho, R² negativo.

## Testes e Validações
- **Validação cruzada**: RMSE médio de todos os testes foi de 0.74.

### Análise Comparativa: Algoritmos Preditores
O XGBoost é o modelo com maior potencial de precisão, apresentando o menor erro médio absoluto (MAE) e o maior R².

### Otimização de Modelo: XGBoost
Otimização dos hiperparâmetros para melhorar a precisão do modelo.

- **Resultado do Modelo com Hiperparâmetros Otimizados**: RMSE de 39.602 (melhoria significativa).
- **Resultado do Modelo Sem Hiperparâmetros Otimizados**: RMSE de 50.546.

## Análise Comparativa: Dados Reais vs. Preditos para as Semanas do Conjunto de Teste
Os dados preditos apresentam um padrão linear consistente, capturando com precisão os padrões principais dos dados.

## Conclusões
- A análise exploratória de dados é fundamental.
- O XGBoost se destacou por sua alta performance na previsão dos volumes de vendas.
- O ajuste cuidadoso dos hiperparâmetros é necessário para garantir um modelo eficiente.

## Próximos Passos
- Melhorar a performance do XGBoost com um maior volume de dados, especialmente dados históricos.
- Incluir a variável inflação na análise, devido ao seu potencial impacto no volume de vendas.

## Visualizações do Dashboard

### Home
![Home]((https://github.com/Rafarockdf/Portifolio_Data_analytics_Data_Science/blob/main/Melhores_Compras_ML_Predicao_Vendas/imagens/home.png))

### Visão Geral - Previsão da base de testes com o resultado
![Visão Geral - Previsão da base de testes com o resultado](https://github.com/Rafarockdf/Portifolio_Data_analytics_Data_Science/blob/main/Melhores_Compras_ML_Predicao_Vendas/imagens/visao_geral_predicao_desabilitado.png)

### Visão Geral - Previsão Futura
![Gráfico de Dispersão](https://github.com/Rafarockdf/Portifolio_Data_analytics_Data_Science/blob/main/Melhores_Compras_ML_Predicao_Vendas/imagens/visao_geral_predicao_habilitado.png)

### Visão Insights
![Visão Insights](https://github.com/Rafarockdf/Portifolio_Data_analytics_Data_Science/blob/main/Melhores_Compras_ML_Predicao_Vendas/imagens/visao_insights.png)

