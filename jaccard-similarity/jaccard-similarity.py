def jaccard_similarity(set_a, set_b):
    """
    Compute the Jaccard similarity between two item sets.
    """
    # Write code here
    set_a=set(set_a)
    set_b=set(set_b)
    u=set_a.union(set_b)
    i=set_a & set_b

    if len(u)==0:
        return 0.0
    return len(i)/len(u)