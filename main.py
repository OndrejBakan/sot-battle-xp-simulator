import logging
import random

WINRATE = 0.6
LOWER_AT_STREAK = 2

def main(target_level):

    logging.basicConfig(level=logging.INFO)

    level = 0
    xp = 0
    battles_lost = 0
    battles_won = 0
    streak = 0

    
    while xp < target_level * 12600:
        logging.info(f"Fight {battles_won + battles_lost}")

        # battle
        result, result_xp, result_streak = battle(WINRATE, streak)

        # result
        streak = result_streak
        battles_won += (1 if result == 'win' else 0)
        battles_lost += (1 if result == 'loss' else 0)

        xp += result_xp

        print(result, result_xp, result_streak)
                
        if streak == LOWER_AT_STREAK:
            xp += cash_in_hourglass(streak)
            streak = 0
            # print(f"Cashed in at streak {LOWER_AT_STREAK}")
            # print(f"XP: {xp}, streak {streak}")
        
        #print()

    print(f"Gained {xp} XP in {battles_won + battles_lost} battles ({battles_won} won, {battles_lost} lost).")

def battle(winrate, streak):

    if random.random() < WINRATE:
        result = 'win'

        if streak == 0:
            xp = 4200
        elif streak == 1:
            xp = 4675
        elif streak == 2:
            xp = 5160
        elif streak == 3:
            xp = 5688
        elif streak >= 4:
            xp = 6600
        
        streak += 1
    else:
        result = 'loss'
        xp = 560
        streak = 0
    
    return (result, xp, streak)

def cash_in_hourglass(streak):
    if streak == 0:
        return 0
    elif streak == 1:
        return 1100
    elif streak == 2:
        return 2640
    elif streak == 3:
        return 4680
    elif streak == 4:
        return 7800
    elif streak >= 5:
        return 7800 + 3000 * (streak - 4)

if __name__ == '__main__':
    main(1000)