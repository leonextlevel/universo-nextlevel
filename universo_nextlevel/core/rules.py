import rules


@rules.predicate
def is_cenario_criador(user, cenario):
    return cenario.criador == user


rules.add_perm('core.can_edit_cenario_instance', is_cenario_criador)
rules.add_perm('core.can_delete_cenario_instance', is_cenario_criador)
