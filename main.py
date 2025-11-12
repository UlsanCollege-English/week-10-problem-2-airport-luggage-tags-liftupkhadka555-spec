"""
HW02 — Airport Luggage Tags (Open Addressing with Delete)
Implement linear probing with EMPTY and DELETED markers.
"""

# Step 4: create unique marker objects
EMPTY = object()
DELETED = object()

def _hash_key(s):
    total = 0
    for ch in s:
        total += ord(ch)
    return total

def make_table_open(m):
    """Return a table of length m filled with EMPTY markers."""
    return [EMPTY] * m

def _find_slot_for_insert(t, key):
    """Return index to insert/overwrite. Return None if full."""
    m = len(t)
    start = _hash_key(key) % m
    first_deleted = None

    for i in range(m):
        idx = (start + i) % m
        slot = t[idx]

        if slot is EMPTY:
            # Prefer a previously found DELETED slot if exists, else this one
            return first_deleted if first_deleted is not None else idx

        if slot is DELETED:
            # Remember first DELETED slot seen
            if first_deleted is None:
                first_deleted = idx
            continue

        # existing key -> allow overwrite
        if slot[0] == key:
            return idx

    return first_deleted  # table full except deleted spaces or truly full

def _find_slot_for_search(t, key):
    """Return index where key is found; else None. DELETED does not stop search."""
    m = len(t)
    start = _hash_key(key) % m

    for i in range(m):
        idx = (start + i) % m
        slot = t[idx]

        if slot is EMPTY:
            return None  # key does not exist
        if slot is DELETED:
            continue
        if slot[0] == key:
            return idx

    return None

def put_open(t, key, value):
    """Insert or overwrite (key, value). Return True if success, False if full."""
    idx = _find_slot_for_insert(t, key)
    if idx is None:
        return False
    t[idx] = [key, value]
    return True

def get_open(t, key):
    """Return value or None if not present."""
    idx = _find_slot_for_search(t, key)
    if idx is None:
        return None
    return t[idx][1]

def delete_open(t, key):
    """Delete key if present. Return True if removed, else False."""
    idx = _find_slot_for_search(t, key)
    if idx is None:
        return False
    t[idx] = DELETED
    return True

if __name__ == "__main__":
    pass