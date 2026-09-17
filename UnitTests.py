import classes
import pygame
screen = pygame.display.set_mode((90, 90))
#Creates a map with wall in the middle 
list_tile =  [(classes.tile(0, 0, 30, 30, 0, 0 , 0, False, False, room = 'no room attacthed', spawn = 'no spawn')), 
              (classes.tile(30, 0, 30, 30, 0, 0 , 0, False, False, room = 'no room attacthed', spawn = 'no spawn')),
              (classes.tile(60, 0, 30, 30, 0, 0 , 0, False, False, room = 'no room attacthed', spawn = 'no spawn')),
              (classes.tile(0, 30, 30, 30, 0, 0 , 0, False, False, room = 'no room attacthed', spawn = 'no spawn')),
              (classes.tile(30, 30, 30, 30, 0, 0 , 0, True, False, room = 'no room attacthed', spawn = 'no spawn')),
              (classes.tile(60, 30, 30, 30, 0, 0 , 0, False, False, room = 'no room attacthed', spawn = 'no spawn')),
              (classes.tile(0, 60, 30, 30, 0, 0 , 0, False, False, room = 'no room attacthed', spawn = 'no spawn')),
              (classes.tile(30, 60, 30, 30, 0, 0 , 0, False, False, room = 'no room attacthed', spawn = 'no spawn')),
              (classes.tile(60, 60, 30, 30, 0, 0 , 0, False, False, room = 'no room attacthed', spawn = 'no spawn'))]



def test_self_collision(test_tiles):
    player = classes.player()
    #Places player at pos 45,45(Collision)
    player.rect.x = 45
    player.rect.y = 45
    collides = player.collision(test_tiles)#map tile list)
    assert collides == True, "failed collision"
    print("passed collision") 
    player.rect.x = 80
    player.rect.y = 80
    collides = player.collision(test_tiles)#map tile list)
    assert collides == False, "There was a collision when there shouldn't have been"
    print("There was no collision")
    player.rect.x = -5
    player.rect.y = -5
    collides = player.collision(test_tiles)#map tile list)
    assert collides == True, "Didn't collide with wall when it should've"
    print("Collided with wall!")
test_self_collision(list_tile)
def test_hit():
    #The testing entities to be hit
    base_dummy =  classes.base_monster(5,5,20,20)
    boss_dummy =  classes.boss(55, 5, 20, 20)
    player_dummy =  classes.player()
    #The following four statements are to change the placement and size of the player rect(hitbox)
    player_dummy.rect.height = 20
    player_dummy.rect.width = 20
    player_dummy.rect.x = 5
    player_dummy.rect.y = 55
    #Projectile is place not at any entity, so hit should return false
    projectile = classes.base_weapon(100, 100, 1, 1) #(x loc, y loc, mouse x loc, mouse y loc)
    assert base_dummy.hit(projectile) == False, " Base Dummy hit when it shouldn't have been"
    assert boss_dummy.hit(projectile) == False, "Boss Dummy hit when it shouldn't have been"
    assert player_dummy.hit(projectile) == False, "Player Dummy hit when it shouldn't have been"
    print("All three passed not being hit!")
    #Now testing each indiviudal dummy for being hit by placing projectile on top of them
    projectile = classes.base_weapon(10, 10, 100, 100)
    assert base_dummy.hit(projectile) == True, " Base Dummy wasn't hit when it should have been"
    print("Base dummy was hit!")
    projectile = classes.base_weapon(50, 10, 100, 100)
    assert boss_dummy.hit(projectile) == True, " Boss Dummy wasn't hit when it should have been"
    print("Boss dummy was hit!")
    projectile = classes.base_weapon(10, 60, 100, 100)
    assert player_dummy.hit(projectile) == True, " Player Dummy wasn't hit when it should have been"
    print("Player dummy was hit!")
test_hit()
def test_player_hit():
    player_dummy = classes.player()
    original_health = player_dummy.health
    classes.hit(player_dummy, 3, 60)
    assert player_dummy.health == original_health - 3, "Health didn't reduce correctly"
    assert player_dummy.invincibilty == True, "Invincibility wasn't set"
    print("Hit function works correctly!")
    if not player_dummy.invincibilty:
        classes.hit(player_dummy, 3, 60)  # hit again while invincible
    assert player_dummy.health == original_health - 3, "Health changed during invincibility"
    print("Invincibility correctly prevented second hit!")
test_player_hit()
def test_move(test_tiles):
    #Down is technically an increasing Y and up decreasing, but I'm describing the movements based off of what would happen visually
    test_monster = classes.base_monster(20, 20, 3, 3) #Places the monster at location (20,20), dont wan't hitting an object to be a problem so made hitbox small
    test_monster.move(20, 10, .1, test_tiles) #Places hypthetical player at (20,10)
    ExpectedMonsterYAfterOneIteration = 12 # .1 times speed(80) = 8, 20-8 = 12
    assert test_monster.rect.y == ExpectedMonsterYAfterOneIteration, ("Monster did not move y expected Amount, move this amount: ", str(test_monster.rect.y))
    print("Moved in y DOWN at the correct rate!")
    test_monster = classes.base_monster(20, 20, 3, 3) #Places the monster at location (20,20), dont wan't hitting an object to be a problem so made hitbox small
    test_monster.move(20, 30, .1, test_tiles) #Places hypthetical player at (20,10)
    ExpectedMonsterYAfterOneIteration = 28 # .1 times speed(80) = 8, 20+8 = 28
    assert test_monster.rect.y == ExpectedMonsterYAfterOneIteration, ("Monster did not move y expected Amount, move this amount: ", str(test_monster.rect.y))
    print("Moved in y UP at the correct rate!")
    test_monster = classes.base_monster(20, 20, 3, 3) #Places the monster at location (20,20), dont wan't hitting an object to be a problem so made hitbox small
    test_monster.move(10, 20, .1, test_tiles) #Places hypthetical player at (20,10)
    ExpectedMonsterXAfterOneIteration = 12 # .1 times speed(80) = 8, 20-8 = 12
    assert test_monster.rect.x == ExpectedMonsterXAfterOneIteration, ("Monster did not move x expected Amount, move this amount: ", str(test_monster.rect.x))
    print("Moved in x LEFT at the correct rate!")
    test_monster = classes.base_monster(20, 20, 3, 3) #Places the monster at location (20,20), dont wan't hitting an object to be a problem so made hitbox small
    test_monster.move(30, 20, .1, test_tiles) #Places hypthetical player at (20,10)
    ExpectedMonsterXAfterOneIteration = 28 # .1 times speed(80) = 8, 20+8 = 28
    assert test_monster.rect.x == ExpectedMonsterXAfterOneIteration, ("Monster did not move x expected Amount, move this amount: ", str(test_monster.rect.x))
    print("Moved in x RIGHT at the correct rate!")
test_move(list_tile)
