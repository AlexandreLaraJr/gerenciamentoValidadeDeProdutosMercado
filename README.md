# gerenciamentoValidadeDeProdutosMercado

Este projeto tem como objetivo gerenciar e transformar dados de validade de produtos de mercado, utilizando técnicas de ETL (Extração, Transformação e Carga) e web scraping.

## Estrutura do Projeto

-   **concatScrapping.py**: Script para concatenar dados obtidos via scraping.
-   **dataAddAndTranform.py**: Script para adicionar e transformar dados dos produtos.
-   **produtos.csv**: Base de dados original dos produtos.
-   **produtosETL.csv**: Base de dados após processos de ETL.
-   **produtosETLbkp.csv**: Backup da base de dados ETL.
-   **scrapping/**: Pasta com scripts de scraping para diferentes categorias de produtos (bolachas, chocolates, salgadinhos).

## Como usar

1. Instale as dependências necessárias (recomenda-se o uso de um ambiente virtual).
2. Caso queira editar a quantidade de dados obtidos no scrapping, utilize os scripts de scraping localizados na pasta `scrapping/`.
3. Utilize o `concatScrapping.py` para realizar o web scrapping dos três arquivos da `scrapping/`.
4. Execute o `dataAddAndTranform.py` para processar e transformar os dados.
5. Os resultados estarão disponíveis nos arquivos `produtosETL.csv`.

## Observações

-   Os arquivos `.csv` principais estão listados no `.gitignore` e não são versionados.
-   Scripts de scraping são separados por categoria de produto para facilitar a manutenção.
-   Caso queira utilizar o mesmo `.csv` que utilizei, utilize o `produtosETLbkp.csv`

## Licença

Este projeto é apenas para fins educacionais.
