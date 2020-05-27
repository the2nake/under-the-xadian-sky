'''
Module defining tileset for the game "Under a Xadian Sky"

Dependecies: None
'''

names = "empty dirt1 dirt2 dirt3 dirt4 grass1 grass2 grass3 road road-corner road-three-intersection road-intersection road-end thin-wall thin-wall-with-bump thin-wall-corner brick-tile kitchen-tile top-left-stone-floor top-middle-stone-floor top-right-stone-floor ladder-end spike alert-outline person-raincoat person1 person-spearman person-swordsman person-crusader person-pikeman person-armoured person-warlord "


names = names + "tree1 tree2 tree3 tree4 tree5 tree6 cactus cacti path path-corner path-three-intersection path-intersection path-end lane lane-corner lane-three-intersection lane-intersection footsteps center-left-stone-floor platform-stone center-right-stone-floor ladder shaft alert-fill person-great-mage person-boy-scout person-princess person-office person-grunt person-teen person-apprentice person-mage "


names = names + "tree7 tree8 tree9 tree10 great-tree stones dead-tree tree11 carpet carpet-corner carpet-three-intersection carpet-intersection carpet-end pillar-end pillar-wall pillar-corner pillar-intersection pillar-three-intersection bottom-left-stone-floor bottom-middle-stone-floor bottom-right-stone-floor dry-grass shaft-barred box person-elder troll-whelp troll devil pirate yoda person-fencer person-farmer "


names = names + "fence-low fence fence-flat door-gate-closed door-gate-open bars bars-broken indoor-wall indoor-outer-corner indoor-inner-corner indoor-wall-small-hallway indoor-wall-dead-end indoor-wall-with-inner-corner wall-end wall wall-corner wall-intersection wall-three-intersection top-left-stone top-right-stone slant-top-left-stone-floor slant-top-right-stone-floor box-chiseled chessboard person-rogue robot-single-wheel robot robot-strong king queen boy girl "


names = names + "fence-metal-low fence-metal fence-metal-broken door-gate-metal-closed door-gate-metal-open gate-metal-closed bridge-metal-elevated bridge-metal river river-turn river-three-intersection river-intersection river-end wall-outline-end wall-outline wall-outline-corner wall-outline-intersection wall-outline-three-intersection bottom-left-stone bottom-right-stone slant-bottom-left-stone-floor slant-bottom-right-stone-floor coin diamond person-hooded person-old engineer person-wrestler person-businessman person-wheelchair person2 person3 "


names = names + "rail rail-corner rail-three-intersection rail-intersection rail-broken bar-ground bridge-wooden-elevated bridge-wooden river-empty river-shore river-outer-corner river-inner-corner stream stream-turn stream-reservoir roller-coaster-ramp roller-coaster-track roller-coaster-track-broken platform leaves1 leaves2 spring1 spring2 spring3 lobster crab bee turtle spider1 spider2 spider3 wasp "


names = names + "rail-wooden rail-wooden-broken stairs-up stairs-down drawbridge bookshelf arch-wooden unknown1 chest-open chest-closed basket-open basket-closed crossing-side plants1 plants2 plants3 plants4 plants5 tree-trunk1 tree-trunk2 tree-trunk3 platform-start platform-middle platform-end person-dark-mage person-dark ghost1 ghost2 ghost3 skeleton giant1 dark-warrior "


names = names + "sign-direction sign mailbox bookcase bookcase-small wardrobe-closed wardrobbe-open cupboard-closed cupboard-open cupboard-hanging-closed cupboard-hanging-open sink refridgerator refridgerator-open sign-bed sign-semi-circle sign-rectangle banner blue-run1 blue-run2 blue-run3 blue-jump1 blue-jump2 blue-die person-empty-with-face duck chicken cow horse pig cat dog "


names = names + "mirror-standing bedtable table-up table-side-end table-side-middle bed bed-start bed-end chimney fireplace pancakes stove1 stove2 basin sign-hanging-bed sign-handing-semicircle table-up-end flag yellow-run1 yellow-run2 yellow-run3 yellow-jump1 yellow-jump2 yellow-die person-empty octopus bat blob snake crocodile bear rat "


names = names + "door-lock door-energy-field door-frame-blue door1 door2 door3 door-frame door4 door5 door-frame-thin door6 chair-side1 chair-up1 toilet-up table-side1 table-side2 table-up-middle flag-triangle green-run1 green-run2 green-run3 green-jump1 green-jump2 green-die cyclops giant2 gnome person-assasin person-theif person-warior person-general mermaid "


names = names + "lock button button-pressed lever-off lever-on door-metal1 door-metal2 door-metal-garage doorframe-metal door-metal-end door-metal-garage-end doorframe-metal-end toilet-side bathtub-side campfire fire table-up-start1 table-up-start2 house-green tent-green sign-asian lantern-hanging lights-hanging bell avatar-boy avatar-girl avatar-man-old avatar-man-bald-man avatar-man avatar-man2 avatar-girl2 avatar-woman "


names = names + "lock-square stairs-stone-up wall-stone-top castle-patrol-up-top bar-locked roof-tile1 roof-tile2 roof-tile3 door-metal-bars1 door-metal3 door-metal4 door-metal5 door-metal-bars-open door-metal-bars2 sign-road tires-stack drawbridge-side-open door-blocked roof-green-start roof-green-middle roof-green-end asian-arch1 asian-arch2 gong gfx-slash gfx-slash-arch gfx-scratch gfx-magical gfx-fire gfx-missile gfx-slash-x gfx-burn "


names = names + "castle-tower-top1 castle-tower-top2 castle-tower-emblem castle-patrol-up-middle table-locked roof-start roof-middle roof-end pipe-end pipe-middle pipe-invalid pipe-support chain idol wires-hanging tire rubble gfx-bubbles curtain-end window-bars1 door7 window-goemetric window-bars2 crossing-up arrow-up1 sectioning-intersection sectioning-intersection-arrows gfx-tree gfx-explode1 gfx-explode2 gfx-confuse gfx-explode3 " 


names = names + "stone-wall stone-window stone-window-small castle-patrol-up-end stone-arch brick-window1 brick-wall1 brick-window2 road-support1 road-support2 crane-beam crane-support hook hard-disks flask crane-wheels castle-wall-top-left castle-wall-top-middle castle-wall-top-right castle-patrol-side-end castle-patrol-side-middle hallway-side-end1 hallway-side-middle hallway-side-end2 arrow-up2 sectioning sectioning-end-curved sectioning-end-fade sectioning-corner-curved sectioning-three-intersection-curved sectioning-corner sectioning-three-intersection"


names = names.split()


def init():
    '''
    This function will initiaze the tilemap

    Arguments: None

    Returns:
    tilemap (dict): The tilemap for every tile on the tilesheet
    '''

    # row 1

    tilemap = {}  # format: (posx, posy, width, height)
    avatarnames = []

    for i, item in enumerate(names):
        tilemap[item] = (17 * (i % 32), 17 * (i // 32), 16, 16)

    
    for name in names:
        if name[0:6] == "avatar":
            avatarnames.append(name)

    return tilemap, (names, avatarnames)


if __name__ == "__main__":
    tilesheet, tilenames = init()
    print(tilesheet.get("empty"))
    print(list(tilesheet.keys())[64])
