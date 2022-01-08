def direction(facing, turn):
    directions = ['N', 'NE', 'E', 'SE', 'S', 'SW', 'W', 'NW']
    turns = turn // 45

    start = directions.index(facing)
    end = (start + turns) % len(directions)
    return directions[end]
