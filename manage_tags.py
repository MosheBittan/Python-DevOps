def manage_tags(existing_tags: dict, *simple_tags, **key_value_tags) -> dict:
    """
    Applies simple and key-value tags to an existing dictionary of tags.

    Args:
        existing_tags: The initial dictionary of tags.
        *simple_tags: Positional string arguments to be added as tags with a
                      value of 'true'. Duplicates should be ignored.
        **key_value_tags: Keyword arguments to be added or used to overwrite
                          existing tags.

    Returns:
        A new dictionary with all tags merged.
    """
    
    # print(f"Required Tags: {existing_tags}")
    # print(f"Simple Extras (Tuple): {simple_tags}")
    # print(f"Key-Value Extras (Dictionary): {key_value_tags}")
    
    # TODO: Implement the tagging logic.
    # 1. Do not modify the original dictionary
    new_tags = existing_tags.copy()
    # 2. Process the 'simple_tags' (*args).
    #it will work without set but if you have million on simple_tags this will remove only to unique and then do the proccess which more fast and performance
    for value in set(simple_tags)
        new_tags.update({value:"true"})
    # 3. Process the 'key_value_tags' (**kwargs).
    new_tags.update(key_value_tags)
    # 4. Return the new, merged dictionary.
    return new_tags
    


initial = {'owner': 'dev-team', 'env': 'dev'}
final_tags = manage_tags(
    initial,
    'billable',              # A simple tag
    'critical',
    'billable',                            # Another simple tag
    env='staging',           # A key-value tag that overwrites an existing key
    cost_center='xyz-123'    # A new key-value tag
)
print("#######\n")
print(final_tags)
