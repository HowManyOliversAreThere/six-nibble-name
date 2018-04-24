C = 'bcdfghjklmnpqrstvwxyz'
V = 'aeiou'

def get(sb=None):
    if not sb:
        from machine import unique_id
        sb = int.from_bytes(unique_id(), 'little')
    n = ''
    n += C[((sb & 0xFE0000) >> 17) % len(C)].upper()
    n += V[((sb & 0x1F000) >> 12) % len(V)]
    n += C[((sb & 0xFE0) >> 5) % len(C)]
    n += V[(sb & 0x1F) % len(V)]
    return n
