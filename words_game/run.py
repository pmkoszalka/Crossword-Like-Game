from words_game.functions import *

if __name__ == '__main__':
    '''Game logic'''

    '''Setting up the variables'''
    randomize()
    diagram_new = diagram_letters_func()
    words_from_diagram = words(diagram_new, 6)  # here you can choose the minimum length of the word
    player_input = ''
    game_on = True
    player_answer_on = True
    words_correct = []
    words_number = len(words_from_diagram)

    '''Checking if the words can be created'''
    if words_number == 0:
        board(diagram_new)
        print('--------------------------------------------')
        print('Reroll the game or change the words\' lenght, becasue there are no words to be made from this diagram!')
        game_on = False


    else:

        ''' Print out the board, rules, and number of possible words'''
        print('Welcome to the word\'s quiz!')
        print('--------------------------------------------')
        print('Rules:')
        print('--------------------------------------------')
        print('Make a word out of the letters in the board.')
        print('You have to use the letter in the centre!')
        print('Words cannot repeat letters and have to consist of at least 4 letters.')
        print('Plurar forms do not work!')
        print('--------------------------------------------')
        board(diagram_new)
        print('')
        print(f'Number of possible words that can be created from the diagram: {words_number}')
        print('--------------------------------------------')

    '''Main game logics'''
    while game_on:

        '''Getting the input of a player'''
        player_answer_on = True
        print('Your word is:')
        player_input = input()
        print('--------------------------------------------')

        '''Checking if input is in the words from letters'''
        if player_input in words_from_diagram:

            words_number = words_number - 1

            '''Checking if the player guessed all the words'''
            if words_number != 0:
                print('That is correct! Great job!')
                print('')
                print(f'You still can make {words_number} words out of the diagram')
                words_from_diagram.remove(player_input)
                words_correct.append(player_input)

            else:

                print('--------------------------------------------')
                print('Congratulations, you have won!')
                break

        else:

            print('Unfortunately, that is not correct.')

            '''Asking player to play again or not'''
            while player_answer_on:

                print('Do you want to play again?')
                play_again = input()

                if play_again in ['Y', 'y', 'yes', 'Yes']:

                    print('--------------------------------------------')
                    print(f'You still can make {words_number} words out of the diagram')
                    print('Give it another try, type your word:')
                    player_answer_on = False
                    continue

                elif play_again in ['N', 'n', 'no', 'No']:

                    print('--------------------------------------------')
                    print('Here are the words that you got right: {}'.format(measure_and_join(words_correct)))
                    print('--------------------------------------------')
                    print('Here are the words that you have missed: {}'.format(', '.join(words_from_diagram)))
                    print('--------------------------------------------')
                    print('Thanks for playing :)!')

                    game_on = False
                    player_answer_on = False
                    break

                else:
                    print('--------------------------------------------')
                    print('You have to choose: yes - to play again or no - to end the gamne :)')
                    pass
