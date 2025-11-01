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
    # TODO: Implement the tagging logic.
    # 1. Do not modify the original dictionary
    all_tags = existing_tags.copy()
    # 2. Process the 'simple_tags' (*args).
    for tag in simple_tags:
        all_tags[tag] = 'true'
    # 3. Process the 'key_value_tags' (**kwargs).
    all_tags.update(key_value_tags)
    # 4. Return the new, merged dictionary.
    return all_tags
