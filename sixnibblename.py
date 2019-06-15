C = 'bcdfghjklmnpqrstvwxyz'
V = 'aeiou'

def get(sb=None):
    if not sb:
        from machine import unique_id
        import sys
        uid = unique_id()
        if sys.platform == 'esp32':
            uid = uid[3:]
        sb = int.from_bytes(uid, 'little')
    n = ''
    n += C[((sb & 0xFE0000) >> 17) % len(C)].upper()
    n += V[((sb & 0x1F000) >> 12) % len(V)]
    n += C[((sb & 0xFE0) >> 5) % len(C)]
    n += V[(sb & 0x1F) % len(V)]
    return n
