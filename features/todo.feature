Feature: Todo List

    Scenario: Criar um Cartão de Todo
        Given que eu esteja na pagina
        When criar um todo
            """
            {
                "produto":"mouse rgb"
            }
            """
        Then o todo deve estar na pilha "A fazer"


