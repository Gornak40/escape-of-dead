**output:** lawn barricade garage kills skip_spawn result tp
- lawn: number of zombies *0..6*
- barricade: barricade hp *0..10*
- garage: garage progress *0..10*
- kills: number of kills *0..10*
- skip_spawn: *1* if spawn skips next turn, *0* otherwise
- result *0* if game is in progress, *1* if player won, *-1* if player lost
- tp negative number if you need to ignore this output, *1* if you need to put the distribution of dices, *2* if you need to put the bonus number

**input:** *4* upper case letters *L,B,G* if tp is one, *1..4* if tp is *2*
- 1: destroy all zombies
- 2: repair *1* garage
- 3: skip spawn next turn
- 4: create *3* barricade