from . import candidate_pool

def dispatch(candidate_pool, rx, msgclass):
    (id, cmd_id, _origin, content_ext) = rx.get()
    pass

