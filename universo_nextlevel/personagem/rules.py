import rules


@rules.predicate
def is_personagem_criador(user, personagem):
    return personagem.cenario.criador == user


rules.add_perm('personagem.can_edit_personagem_instance', is_personagem_criador)
rules.add_perm('personagem.can_delete_personagem_instance', is_personagem_criador)
