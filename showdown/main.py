from showdown import ShowDown


def main():
    show_down = ShowDown()
    show_down.initial_game()
    for _ in range(show_down.rounds):
        show_down.play_a_round()


if __name__ == '__main__':
    main()
