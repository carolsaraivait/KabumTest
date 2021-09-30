Feature: Search Kabum
    Scenario: Utilizar o buscador da Kabum
        Given que esteja na pagina
        When realizar busca de produto
            """
            {
                "produto":"Cartucho de Tinta HP Designjet 711"
            }
            """
        Then o produto deve estar no resultado "Cartucho de Tinta HP Designjet 711"
    Scenario: Carrinho
        When adicionar o produto ao carrinho
        Then o produto deve estar no carrinho "Cartucho de Tinta HP Designjet 711, Magenta - CZ135AB"        


