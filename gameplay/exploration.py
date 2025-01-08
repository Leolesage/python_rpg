def deplacer(position, direction):
    """Déplace le joueur dans une direction donnée."""
    mouvements = {
        "nord": (0, 1),
        "sud": (0, -1),
        "est": (1, 0),
        "ouest": (-1, 0),
    }

    if direction in mouvements:
        dx, dy = mouvements[direction]
        position["x"] += dx
        position["y"] += dy
        print(f"Vous vous déplacez vers le {direction}. Nouvelle position : {position}")
    else:
        print("Direction invalide. Choisissez nord, sud, est ou ouest.")

    return position
