def parse_range_float(param_value):
    """Helper function to parse a range like 'min-max' or 'min-'."""
    if param_value:
        parts = param_value.split('-')
        if len(parts) == 2:
            return (float(parts[0]) if parts[0] else None, float(parts[1]) if parts[1] else None)
        elif len(parts) == 1:
            return (float(parts[0]), None)
    return (None, None)
def parse_range(param_value):
    """Helper function to parse a range like 'min-max' or 'min-'."""
    if param_value:
        parts = param_value.split('-')
        if len(parts) == 2:
            return (int(parts[0]) if parts[0] else None, int(parts[1]) if parts[1] else None)
        elif len(parts) == 1:
            return (int(parts[0]), None)
    return (None, None)