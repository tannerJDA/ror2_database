/* challenge tables */
CREATE TABLE Challenge(
	chal_name VARCHAR(80) NOT NULL,
    chal_cate CHAR(80) NOT NULL,
    chal_desc VARCHAR(500) NOT NULL,
    unlocks VARCHAR(80) NOT NULL,
    PRIMARY KEY(chal_name)
);
CREATE TABLE Survivor(
	chal_name VARCHAR(80),
	surv_name VARCHAR(80) NOT NULL,
    surv_health INT NOT NULL,
    surv_regen FLOAT NOT NULL,
    surv_damage FLOAT NOT NULL,
    surv_armor INT,
    surv_speed INT NOT NULL,
    PRIMARY KEY(surv_name),
    FOREIGN KEY(chal_name) REFERENCES Challenge(chal_name)
);
CREATE TABLE Skill(
	chal_name VARCHAR(80),
    surv_name VARCHAR(80) NOT NULL,
    skill_name VARCHAR(80) NOT NULL,
    skill_type VARCHAR(80) NOT NULL,
    skill_desc VARCHAR(500) NOT NULL,
    skill_cooldown FLOAT,
    proc_coeff FLOAT,
    PRIMARY KEY(skill_name),
    FOREIGN KEY(surv_name) REFERENCES Survivor(surv_name),
    FOREIGN KEY(chal_name) REFERENCES Challenge(chal_name)
);
CREATE TABLE Items(
	chal_name VARCHAR(80),
    item_name VARCHAR(80) NOT NULL,
    rarity VARCHAR(80) not null,
    PRIMARY KEY(item_name),
    FOREIGN KEY(chal_name) REFERENCES Challenge(chal_name)
);
CREATE TABLE PassiveItems(
	item_name VARCHAR(80) NOT NULL,
	stack_type VARCHAR(80),
    item_stat_type VARCHAR(80),
    item_stat_stack VARCHAR(80),
    item_value FLOAT,
    item_add FLOAT,
    FOREIGN KEY(item_name) REFERENCES Items(item_name)
);
CREATE TABLE ActiveItems(
	item_name VARCHAR(80) NOT NULL,
    item_cooldown INT,
    FOREIGN KEY(item_name) REFERENCES Items(item_name)
);
/* artifact tables */
CREATE TABLE Environment(
	env_name VARCHAR(80) NOT NULL,
    env_desc VARCHAR(500) NOT NULL,
    stage INT,
    hidden BOOL,
    PRIMARY KEY(env_name)
);
CREATE TABLE Artifact(
	art_name VARCHAR(80) NOT NULL,
    env_name VARCHAR(80) NOT NULL,
    art_desc VARCHAR(500) NOT NULL,
    unlock_pattern VARCHAR(500) NOT NULL,
    PRIMARY KEY(art_name),
    FOREIGN KEY(env_name) REFERENCES Environment(env_name)
);
/* monster table */
CREATE TABLE Monster(
	mons_name VARCHAR(80) NOT NULL,
    mons_health INT NOT NULL,
    mons_regen FLOAT,
    mons_damage FLOAT NOT NULL,
    mons_armor INT,
    mons_speed INT,
    mons_type VARCHAR(80) NOT NULL,
    PRIMARY KEY(mons_name)
);
/* run history table */
CREATE TABLE RunHisory(
	surv_name VARCHAR(80) NOT NULL,
    hours INT,
    minutes INT NOT NULL,
    diff VARCHAR(80) NOT NULL
);

/* insert challenges - survivor category */
INSERT INTO `Challenge` (`chal_name`, `chal_cate`, `chal_desc`, `unlocks`) VALUES ('...To Be Left Alone', 'Survivor', 'Stabilize the Cell in the Void Fields.', 'Acrid');
INSERT INTO `Challenge` (`chal_name`, `chal_cate`, `chal_desc`, `unlocks`) VALUES ('Engineering Perfection', 'Survivor', 'Complete 30 stages.', 'Engineer');
INSERT INTO `Challenge` (`chal_name`, `chal_cate`, `chal_desc`, `unlocks`) VALUES ('Guidance Offline', 'Survivor', 'Defeat the unique guardian of Siren\'s Call.', 'Loader');
INSERT INTO `Challenge` (`chal_name`, `chal_cate`, `chal_desc`, `unlocks`) VALUES ('Pause', 'Survivor', 'Free the survivor supspended in time.', 'Artificer');
INSERT INTO `Challenge` (`chal_name`, `chal_cate`, `chal_desc`, `unlocks`) VALUES ('Power Plant', 'Survivor', 'Repair the broken robot with an Escape Pod\'s Fuel Array.', 'REX');
INSERT INTO `Challenge` (`chal_name`, `chal_cate`, `chal_desc`, `unlocks`) VALUES ('True Respite', 'Survivor', 'Obliterate yourself at the Obelisk.', 'Mercenary');
INSERT INTO `Challenge` (`chal_name`, `chal_cate`, `chal_desc`, `unlocks`) VALUES ('Verified', 'Survivor', 'Complete the first Teleporter event 5 times.', 'MUL-T');
INSERT INTO `Challenge` (`chal_name`, `chal_cate`, `chal_desc`, `unlocks`) VALUES ('Warrior', 'Survivor', 'Reach and complete the 3rd Teleporter event without dying.', 'Bandit');
INSERT INTO `Challenge` (`chal_name`, `chal_cate`, `chal_desc`, `unlocks`) VALUES ('Washed Away', 'Survivor', 'Beat the game.', 'Captain');
/* insert challenges - items category */
INSERT INTO `Challenge` (`chal_name`, `chal_cate`, `chal_desc`, `unlocks`) VALUES ('"Is This Bugged?"', 'Items', 'Fail the Shrine of Chance 3 times in a row.', 'Paul\'s Goat Hoof');
INSERT INTO `Challenge` (`chal_name`, `chal_cate`, `chal_desc`, `unlocks`) VALUES ('...Maybe One More.', 'Items', 'Duplicate the same item 7 times in a row with a 3D Printer.', 'Bundle of Fireworks');
INSERT INTO `Challenge` (`chal_name`, `chal_cate`, `chal_desc`, `unlocks`) VALUES ('Advancement', 'Items', 'Complete a Teleporter event.', 'Armor-Piercing Rounds');
INSERT INTO `Challenge` (`chal_name`, `chal_cate`, `chal_desc`, `unlocks`) VALUES ('Automation Activation', 'Items', 'Activate 6 turrets in a single run.', 'Squid Polyp');
INSERT INTO `Challenge` (`chal_name`, `chal_cate`, `chal_desc`, `unlocks`) VALUES ('Blockade Breaker', 'Items', 'Kill 15 boss monsters in a single run.', 'Visions of Heresy and Hooks of Heresy');
INSERT INTO `Challenge` (`chal_name`, `chal_cate`, `chal_desc`, `unlocks`) VALUES ('Cut Down', 'Items', 'Defeat 500 elite monsters.', 'Old Guillotine');
INSERT INTO `Challenge` (`chal_name`, `chal_cate`, `chal_desc`, `unlocks`) VALUES ('Death Do Us Part', 'Items', 'Discover the hidden chamber in the Abandoned Aqueduct.', 'Runald\'s Band and Kjaro\'s Band');
INSERT INTO `Challenge` (`chal_name`, `chal_cate`, `chal_desc`, `unlocks`) VALUES ('Deicide', 'Items', 'Defeat an Elite boss on Monsoon difficulty.', 'Brainstalks');
INSERT INTO `Challenge` (`chal_name`, `chal_cate`, `chal_desc`, `unlocks`) VALUES ('Deja Vu?', 'Items', 'Loop back to the first stage.', 'Sentient Meat Hook');
INSERT INTO `Challenge` (`chal_name`, `chal_cate`, `chal_desc`, `unlocks`) VALUES ('Elite Slayer', 'Items', 'Defeat an Elite-type monster.', 'Medkit');
INSERT INTO `Challenge` (`chal_name`, `chal_cate`, `chal_desc`, `unlocks`) VALUES ('Experimenting', 'Items', 'Pick up 5 different types of Equipment.', 'Fuel Cell');
INSERT INTO `Challenge` (`chal_name`, `chal_cate`, `chal_desc`, `unlocks`) VALUES ('Flawless', 'Items', 'Fully charge a Teleporter without getting hit.', 'Backup Magazine');
INSERT INTO `Challenge` (`chal_name`, `chal_cate`, `chal_desc`, `unlocks`) VALUES ('Glorious Battle', 'Items', 'Charge the Teleporter with less than 10% health.', 'Berzerker\'s Pauldron');
INSERT INTO `Challenge` (`chal_name`, `chal_cate`, `chal_desc`, `unlocks`) VALUES ('Going Fast Recommended', 'Items', 'Reach +300% movespeed (includes sprinting).', 'Wax Quail');
INSERT INTO `Challenge` (`chal_name`, `chal_cate`, `chal_desc`, `unlocks`) VALUES ('Her Concepts', 'Items', 'Find the Altar to N\'kuhana.', 'N\'kuhana\'s Opinion');
INSERT INTO `Challenge` (`chal_name`, `chal_cate`, `chal_desc`, `unlocks`) VALUES ('Keyed Up', 'Items', 'Defeat the Teleporter boss under 15 seconds.', 'Rusted Key');
/* insert challenges - equipment category */
INSERT INTO `Challenge` (`chal_name`, `chal_cate`, `chal_desc`, `unlocks`) VALUES ('Ascendant', 'Equipment', 'Defeat the Teleporter bosses after activating 2 Shrines of the Mountain.', 'Royal Capacitor');
INSERT INTO `Challenge` (`chal_name`, `chal_cate`, `chal_desc`, `unlocks`) VALUES ('Blackout', 'Equipment', 'Defeat the unique guardian of Gilded Coast without any beacons deactivating.', 'Eccentric Vase');
INSERT INTO `Challenge` (`chal_name`, `chal_cate`, `chal_desc`, `unlocks`) VALUES ('Bookworm', 'Equipment', 'Collect 10 Monster or Environment Logs.', 'Radar Scanner');
INSERT INTO `Challenge` (`chal_name`, `chal_cate`, `chal_desc`, `unlocks`) VALUES ('Cleanup Duty', 'Equipment', 'Destroy 20 flying rocks in Sky Meadow.', 'Recycler');
INSERT INTO `Challenge` (`chal_name`, `chal_cate`, `chal_desc`, `unlocks`) VALUES ('Cosmic Explorer', 'Equipment', 'Discover and enter three unique portals.', 'Spinel Tonic');
/* insert challeneges - skills category*/
INSERT INTO `Challenge` (`chal_name`, `chal_cate`, `chal_desc`, `unlocks`) VALUES ('Acrid: Bad Medicine', 'Equipment', 'As Acrid, land the final blow on a Scavenger.', 'Ravenous Bite');
INSERT INTO `Challenge` (`chal_name`, `chal_cate`, `chal_desc`, `unlocks`) VALUES ('Artificer: Chunked!', 'Equipment', 'As Artificer, fully defeat the teleporter boss in a one-second burst of damage.', 'Cast Nano-Spear');
INSERT INTO `Challenge` (`chal_name`, `chal_cate`, `chal_desc`, `unlocks`) VALUES ('Bandit: B&E', 'Equipment', 'As Bandit, kill the final boss with \'Lights Out\'.', 'Desperado');
INSERT INTO `Challenge` (`chal_name`, `chal_cate`, `chal_desc`, `unlocks`) VALUES ('Captain: Smushed', 'Equipment', 'As Captain, kill the final boss using a Supply Beacon', 'OGM-72 \'DIABLO\' Strike');
INSERT INTO `Challenge` (`chal_name`, `chal_cate`, `chal_desc`, `unlocks`) VALUES ('Commando: Godspeed', 'Equipment', 'As Commando, fully charge the first-stage teleporter before the timer hits 5 minutes.', 'Tactical Slide');
INSERT INTO `Challenge` (`chal_name`, `chal_cate`, `chal_desc`, `unlocks`) VALUES ('Engineer: 100% Calculated', 'Equipment', 'As Engineer, defeat the teleporter boss in less than 5 seconds after it spawns.', 'Spider Mines');
INSERT INTO `Challenge` (`chal_name`, `chal_cate`, `chal_desc`, `unlocks`) VALUES ('Huntress: Finishing Touch', 'Equipment', 'As Huntress, land a killing blow with every possible hit of a single glaive.', 'Flurry');
INSERT INTO `Challenge` (`chal_name`, `chal_cate`, `chal_desc`, `unlocks`) VALUES ('Loader: Earthshatter', 'Equipment', 'As Loader, land a Charged Gauntlet hit at 300mph or higher.', 'Thunder Gauntlet');
INSERT INTO `Challenge` (`chal_name`, `chal_cate`, `chal_desc`, `unlocks`) VALUES ('MUL-T: Gotcha!', 'Equipment', 'As MUL-T, land the killing blow on an Imp Overlord with the Preon Accumulator.', 'Power-Saw');
INSERT INTO `Challenge` (`chal_name`, `chal_cate`, `chal_desc`, `unlocks`) VALUES ('Mercenary: Demon of the Skies', 'Equipment', 'As Mercenary, don\'t touch the ground for 30 seconds.', 'Rising Thunder');
INSERT INTO `Challenge` (`chal_name`, `chal_cate`, `chal_desc`, `unlocks`) VALUES ('REX: Bushwhacked', 'Equipment', 'As REX, complete an entire teleporter event while under 50% health.', 'DIRECTIVE: Drill');
/* insert challenges - skins category */
INSERT INTO `Challenge` (`chal_name`, `chal_cate`, `chal_desc`, `unlocks`) VALUES ('Acrid: Mastery', 'Equipment', 'As Acrid, beat the game or obliterate on Monsoon.', 'Albino');
INSERT INTO `Challenge` (`chal_name`, `chal_cate`, `chal_desc`, `unlocks`) VALUES ('Artificer: Mastery', 'Equipment', 'As Artificer, beat the game or obliterate on Monsoon.', 'Chrome');
INSERT INTO `Challenge` (`chal_name`, `chal_cate`, `chal_desc`, `unlocks`) VALUES ('Bandit: Mastery', 'Equipment', 'As Bandit, beat the game or obliterate on Monsoon.', 'Chilly');
INSERT INTO `Challenge` (`chal_name`, `chal_cate`, `chal_desc`, `unlocks`) VALUES ('Captain: Mastery', 'Equipment', 'As Captain, beat the game or obliterate on Monsoon.', 'Admiral');
INSERT INTO `Challenge` (`chal_name`, `chal_cate`, `chal_desc`, `unlocks`) VALUES ('Commando: Mastery', 'Equipment', 'As Commando, beat the game or obliterate on Monsoon.', 'Hornet');
/* insert challenges - artifacts category */
INSERT INTO `Challenge` (`chal_name`, `chal_cate`, `chal_desc`, `unlocks`) VALUES ('Trial of Chaos', 'Artifacts', 'Complete the Trial of Chaos.', 'Artifact of Chaos');
INSERT INTO `Challenge` (`chal_name`, `chal_cate`, `chal_desc`, `unlocks`) VALUES ('Trial of Command', 'Artifacts', 'Complete the Trial of Command.', 'Artifact of Command');
INSERT INTO `Challenge` (`chal_name`, `chal_cate`, `chal_desc`, `unlocks`) VALUES ('Trial of Death', 'Artifacts', 'Complete the Trial of Death.', 'Artifact of Death');
INSERT INTO `Challenge` (`chal_name`, `chal_cate`, `chal_desc`, `unlocks`) VALUES ('Trial of Dissonance', 'Artifacts', 'Complete the Trial of Dissonance.', 'Artifact of Dissonance');
INSERT INTO `Challenge` (`chal_name`, `chal_cate`, `chal_desc`, `unlocks`) VALUES ('Trial of Enigma', 'Artifacts', 'Complete the Trial of Enigma.', 'Artifact of Enigma');

/* insert survivors */
INSERT INTO `Survivor` (`chal_name`, `surv_name`, `surv_health`, `surv_regen`, `surv_damage`, `surv_armor`, `surv_speed`) VALUES ('...To Be Left Alone', 'Acrid', 160, 2.5, 15, 20, 7);
INSERT INTO `Survivor` (`chal_name`, `surv_name`, `surv_health`, `surv_regen`, `surv_damage`, `surv_armor`, `surv_speed`) VALUES ('Pause', 'Artificer', 110, 1, 12, 0, 7);
INSERT INTO `Survivor` (`chal_name`, `surv_name`, `surv_health`, `surv_regen`, `surv_damage`, `surv_armor`, `surv_speed`) VALUES ('Warrior', 'Bandit', 110, 1, 12, 0, 7);
INSERT INTO `Survivor` (`chal_name`, `surv_name`, `surv_health`, `surv_regen`, `surv_damage`, `surv_armor`, `surv_speed`) VALUES ('Washed Away', 'Captain', 110, 1, 12, 0, 7);
INSERT INTO `Survivor` (`surv_name`, `surv_health`, `surv_regen`, `surv_damage`, `surv_armor`, `surv_speed`) VALUES ('Commando', 110, 1, 12, 0, 7);
INSERT INTO `Survivor` (`chal_name`, `surv_name`, `surv_health`, `surv_regen`, `surv_damage`, `surv_armor`, `surv_speed`) VALUES ('Engineering Perfection', 'Engineer', 130, 1, 14, 0, 7);
INSERT INTO `Survivor` (`surv_name`, `surv_health`, `surv_regen`, `surv_damage`, `surv_armor`, `surv_speed`) VALUES ('Heretic', 440, -6, 18, 0, 8);
INSERT INTO `Survivor` (`surv_name`, `surv_health`, `surv_regen`, `surv_damage`, `surv_armor`, `surv_speed`) VALUES ('Huntress', 90, 1, 12, 0, 7);
INSERT INTO `Survivor` (`chal_name`, `surv_name`, `surv_health`, `surv_regen`, `surv_damage`, `surv_armor`, `surv_speed`) VALUES ('Guidance Offline', 'Loader', 160, 2.5, 12, 20, 7);
INSERT INTO `Survivor` (`chal_name`, `surv_name`, `surv_health`, `surv_regen`, `surv_damage`, `surv_armor`, `surv_speed`) VALUES ('True Respite', 'Mercenary', 110, 1, 12, 20, 7);
INSERT INTO `Survivor` (`chal_name`, `surv_name`, `surv_health`, `surv_regen`, `surv_damage`, `surv_armor`, `surv_speed`) VALUES ('Verified', 'MUL-T', 200, 1, 11,  12, 7);
INSERT INTO `Survivor` (`chal_name`, `surv_name`, `surv_health`, `surv_regen`, `surv_damage`, `surv_armor`, `surv_speed`) VALUES ('Power Plant', 'REX', 130, 1, 12, 20, 7);

/* insert skills */
INSERT INTO `Skill` (`surv_name`, `skill_name`, `skill_type`, `skill_desc`, `proc_coeff`) VALUES ('Acrid', 'Vicious Wounds', 'Primary', 'Maul an enemy for 200% damage. Every 3rd hit is Regenerative and deals 400% damage', 1);
INSERT INTO `Skill` (`surv_name`, `skill_name`, `skill_type`, `skill_desc`, `skill_cooldown`, `proc_coeff`) VALUES ('Acrid', 'Neurotoxing', 'Secondary', 'Poisonous. Spit toxic bile for 240% damage.', 2, 1);
INSERT INTO `Skill` (`surv_name`, `skill_name`, `skill_type`, `skill_desc`, `skill_cooldown`, `proc_coeff`) VALUES ('Artificer', 'Flame Bolt', 'Primary', 'Fire a bolt for 220% damage that ignites enemies. Hold up to 4.', 1.3, 1);
INSERT INTO `Skill` (`surv_name`, `skill_name`, `skill_type`, `skill_desc`, `skill_cooldown`, `proc_coeff`) VALUES ('Artificer', 'Plasma Bolt', 'Primary', 'Fire a bolt for 220% damage that explodes in a small area. Hold up to 4.', 1.3, 1);
INSERT INTO `Skill` (`surv_name`, `skill_name`, `skill_type`, `skill_desc`, `skill_cooldown`, `proc_coeff`) VALUES ('Artificer', 'Charged Nano-Bomb', 'Secondary', 'Stunning. Charge up a exploding nano-bomb that deals 400%-2000% damage.', 5, 1);
INSERT INTO `Skill` (`surv_name`, `skill_name`, `skill_type`, `skill_desc`, `skill_cooldown`, `proc_coeff`) VALUES ('Bandit', 'Burst', 'Primary', 'Fire a shotgun burst for 5x100% damage. Can hold up to 4 shells.', .5, .5);
INSERT INTO `Skill` (`surv_name`, `skill_name`, `skill_type`, `skill_desc`, `skill_cooldown`, `proc_coeff`) VALUES ('Bandit', 'Serrated Dagger', 'Secondary', 'Lunge and slash for 360% damage. Critical Strikes also cause hemorrhaging.', 4, 1);
INSERT INTO `Skill` (`surv_name`, `skill_name`, `skill_type`, `skill_desc`, `proc_coeff`) VALUES ('Captain', 'Vulcan Shotgun', 'Primary', 'Fire a blast of pellets that deal 8x120% damage. Charging the attack narrows the spread.', .75);
INSERT INTO `Skill` (`surv_name`, `skill_name`, `skill_type`, `skill_desc`, `skill_cooldown`, `proc_coeff`) VALUES ('Captain', 'Power Tazer', 'Secondary', 'Shocking. Fire a fast tazer that deals 100% damage. Travels farther if bounced.', 6, 1);
INSERT INTO `Skill` (`surv_name`, `skill_name`, `skill_type`, `skill_desc`, `proc_coeff`) VALUES ('Commando', 'Double Tap', 'Primary', 'Rapidly shoot an enemy for 100% damage.', 1);
INSERT INTO `Skill` (`surv_name`, `skill_name`, `skill_type`, `skill_desc`, `skill_cooldown`, `proc_coeff`) VALUES ('Commando', 'Phase Round', 'Secondary', 'Fire a piercing bullet for 300% damage. Deals 40% more damage every time it passes through an enemy.', 3, 1);
INSERT INTO `Skill` (`surv_name`, `skill_name`, `skill_type`, `skill_desc`, `proc_coeff`) VALUES ('Engineer', 'Bouncing Grenades', 'Primary', 'Charge up to 8 grenades that deal 100% damage each', 1);
INSERT INTO `Skill` (`surv_name`, `skill_name`, `skill_type`, `skill_desc`, `skill_cooldown`, `proc_coeff`) VALUES ('Engineer', 'Pressure Mines', 'Secondary', 'Place a two-stage mine that deals 300% damage, or 900% damage if fully armed. Can place up to 4.', 8, 1);
INSERT INTO `Skill` (`surv_name`, `skill_name`, `skill_type`, `skill_desc`, `skill_cooldown`, `proc_coeff`) VALUES ('Heretic', 'Hungering Gaze', 'Primary', 'Fire a flurry of tracking shards that detonate after a delay, dealing 120% base damage. Hold up to 12 charges (+12 per stack) that reload after 2 seconds.', 2, 1);
INSERT INTO `Skill` (`surv_name`, `skill_name`, `skill_type`, `skill_desc`, `skill_cooldown`, `proc_coeff`) VALUES ('Heretic', 'Slicing Maelstrom', 'Secondary', 'Charge up a projectile that deals 875% damage per second to nearby enemies, exploding after 3 seconds to deal 700% damage and root enemies for 3 (+3 per stack) seconds. Recharges after 5 (+5 per stack) seconds.', 5, 1);
INSERT INTO `Skill` (`surv_name`, `skill_name`, `skill_type`, `skill_desc`, `proc_coeff`) VALUES ('Huntress', 'Strafe', 'Primary', 'Agile. Quickly fire a seeking arrow for 150% damage.', 1);
INSERT INTO `Skill` (`surv_name`, `skill_name`, `skill_type`, `skill_desc`, `skill_cooldown`, `proc_coeff`) VALUES ('Huntress', 'Laser Glaive', 'Secondary', 'Throw a seeking glaive that bounces up to 6 times for 250% damage. Damage increases by 10% per bounce.', 7, .8);
INSERT INTO `Skill` (`surv_name`, `skill_name`, `skill_type`, `skill_desc`, `proc_coeff`) VALUES ('Loader', 'Knuckleboom', 'Primary', 'Swing at nearby enemies for 320% damage.', 1);
INSERT INTO `Skill` (`surv_name`, `skill_name`, `skill_type`, `skill_desc`, `skill_cooldown`) VALUES ('Loader', 'Grapple Fist', 'Secondary', 'Fire your gauntlet forward, pulling you to the target.', 5);
INSERT INTO `Skill` (`surv_name`, `skill_name`, `skill_type`, `skill_desc`, `proc_coeff`) VALUES ('Mercenary', 'Laser Sword', 'Primary', 'Agile. Slice in front for 130% damage. Every 3rd hit strikes in a greater area and Exposes enemies.', 1);
INSERT INTO `Skill` (`surv_name`, `skill_name`, `skill_type`, `skill_desc`, `skill_cooldown`, `proc_coeff`) VALUES ('Mercenary', 'Whirlwind', 'Secondary', 'Quickly slice horizontally twice, dealing 2x200% damage. If airborne, slice vertically instead.', 2.5, 1);
INSERT INTO `Skill` (`surv_name`, `skill_name`, `skill_type`, `skill_desc`, `proc_coeff`) VALUES ('MUL-T', 'Auto-Nailgun', 'Primary', 'Rapidly fire nails for 70% damage. Finishes with a blast of 12 nails.', .6);
INSERT INTO `Skill` (`surv_name`, `skill_name`, `skill_type`, `skill_desc`, `skill_cooldown`, `proc_coeff`) VALUES ('MUL-T', 'Blast Canister', 'Secondary', 'Stunning. Launch a canister for 220% damage. Drops stun bomblets for 5x44% damage.', 6, 1);
INSERT INTO `Skill` (`surv_name`, `skill_name`, `skill_type`, `skill_desc`, `proc_coeff`) VALUES ('REX', 'DIRECTIVE: Inject', 'Primary', 'Fire 3 syringes for 3x80% damage. The last syringe Weakens and heals for 60% of damage dealt.', .5);
INSERT INTO `Skill` (`surv_name`, `skill_name`, `skill_type`, `skill_desc`, `skill_cooldown`, `proc_coeff`) VALUES ('REX', 'DIRECTIVE: Drill', 'Secondary', 'Launch a series of seed bullets into the sky, raining down for 450% damage per second.', 6, .5);

/* insert items - common */
INSERT INTO `Items` (`item_name`, `rarity`) VALUES ('Armor-Piercing Rounds', 'Common');
INSERT INTO `Items` (`item_name`, `rarity`) VALUES ('Backup Magazine', 'Common');
INSERT INTO `Items` (`item_name`, `rarity`) VALUES ('Bison Steak', 'Common');
/* insert items - uncommon */
INSERT INTO `Items` (`item_name`, `rarity`) VALUES ('AtG Missile Mk. 1', 'Uncommon');
INSERT INTO `Items` (`item_name`, `rarity`) VALUES ('Bandolier', 'Uncommon');
INSERT INTO `Items` (`chal_name`, `item_name`, `rarity`) VALUES ('Glorious Battle', 'Berzerker\'s Pauldron', 'Uncommon');
/* insert items - legenday */
INSERT INTO `Items` (`item_name`, `rarity`) VALUES ('Aegis', 'Legendary');
INSERT INTO `Items` (`item_name`, `rarity`) VALUES ('Alien Head', 'Legendary');
INSERT INTO `Items` (`chal_name`, `item_name`, `rarity`) VALUES ('Deicide', 'Brainstalks', 'Legendary');
/* insert items - boss */
INSERT INTO `Items` (`item_name`, `rarity`) VALUES ('Charged Perforator', 'Boss');
INSERT INTO `Items` (`item_name`, `rarity`) VALUES ('Empathy Cores', 'Boss');
INSERT INTO `Items` (`item_name`, `rarity`) VALUES ('Genesis Loop', 'Boss');
/* insert items - lunar */
INSERT INTO `Items` (`item_name`, `rarity`) VALUES ('Beads of Fealty', 'Lunar');
INSERT INTO `Items` (`item_name`, `rarity`) VALUES ('Brittle Crown', 'Lunar');
INSERT INTO `Items` (`item_name`, `rarity`) VALUES ('Corpsebloom', 'Lunar');
/* insert items - equipment */
INSERT INTO `Items` (`item_name`, `rarity`) VALUES ('Blast Shower', 'Equipment');
INSERT INTO `Items` (`item_name`, `rarity`) VALUES ('Disposable Missile Launcher', 'Equipment');
INSERT INTO `Items` (`item_name`, `rarity`) VALUES ('Eccentric Vase', 'Equipment');

/* insert passive items */
INSERT INTO `PassiveItems` (`item_name`, `stack_type`, `item_stat_type`, `item_stat_stack`, `item_value`, `item_add`) VALUES ('Armor-Piercing Rounds', 'Linear', 'Damage', 'Linear', 20, 20);
INSERT INTO `PassiveItems` (`item_name`, `stack_type`, `item_stat_type`, `item_stat_stack`, `item_value`, `item_add`) VALUES ('Backup Magazine', 'Linear', 'Charge', 'Linear', 1, 1);
INSERT INTO `PassiveItems` (`item_name`, `stack_type`, `item_stat_type`, `item_stat_stack`, `item_value`, `item_add`) VALUES ('Bison Steak', 'Linear', 'Heatlh', 'Linear', 25, 25);
INSERT INTO `PassiveItems` (`item_name`, `stack_type`, `item_stat_type`, `item_stat_stack`, `item_value`, `item_add`) VALUES ('AtG Missile Mk. 1', 'Linear', 'Damage', 'Linear', 300, 300);
INSERT INTO `PassiveItems` (`item_name`, `stack_type`, `item_stat_type`, `item_stat_stack`, `item_value`, `item_add`) VALUES ('Bandolier', 'Linear', 'Chance', 'Special', 18, 10);
INSERT INTO `PassiveItems` (`item_name`, `stack_type`, `item_stat_type`, `item_stat_stack`, `item_value`, `item_add`) VALUES ('Berzerker\'s Pauldron', 'Linear', 'Frenzy Duration', 'Linear', 6, 4);
INSERT INTO `PassiveItems` (`item_name`, `stack_type`, `item_stat_type`, `item_stat_stack`, `item_value`, `item_add`) VALUES ('Aegis', 'Linear', 'Healing Converted', 'Linear', 50, 50);
INSERT INTO `PassiveItems` (`item_name`, `stack_type`, `item_stat_type`, `item_stat_stack`, `item_value`, `item_add`) VALUES ('Alien Head', 'Exponential', 'Cooldown', 'Exponential', 25, 25);
INSERT INTO `PassiveItems` (`item_name`, `stack_type`, `item_stat_type`, `item_stat_stack`, `item_value`, `item_add`) VALUES ('Brainstalks', 'Linear', 'Duration', 'Linear', 4, 4);
INSERT INTO `PassiveItems` (`item_name`, `stack_type`, `item_stat_type`, `item_stat_stack`, `item_value`, `item_add`) VALUES ('Charged Perforator', 'Linear', 'Damage', 'Linear', 500, 500);
INSERT INTO `PassiveItems` (`item_name`, `stack_type`, `item_value`, `item_add`) VALUES ('Empathy Cores', 'Probe Damage', 100, 100);
INSERT INTO `PassiveItems` (`item_name`, `stack_type`, `item_stat_type`, `item_stat_stack`, `item_value`, `item_add`) VALUES ('Genesis Loop', 'Linear', 'Recharge Speed', 'Linear', 100, 50);
INSERT INTO `PassiveItems` (`item_name`) VALUES ('Beads of Fealty');
INSERT INTO `PassiveItems` (`item_name`, `stack_type`, `item_stat_type`, `item_stat_stack`, `item_value`, `item_add`) VALUES ('Brittle Crown', 'Linear', 'Gold Gained', 'Linear', 2, 2);
INSERT INTO `PassiveItems` (`item_name`, `stack_type`, `item_stat_type`, `item_stat_stack`, `item_value`, `item_add`) VALUES ('Corpsebloom', 'Linear Hyperbolic', 'Maximum Heal', 'Hyperbolic', 10, -50);

/* insert active items */
INSERT INTO `ActiveItems` (`item_name`, `item_cooldown`) VALUES ('Blast Shower', 20);
INSERT INTO `ActiveItems` (`item_name`, `item_cooldown`) VALUES ('Disposable Missile Launcher', 45);
INSERT INTO `ActiveItems` (`item_name`, `item_cooldown`) VALUES ('Eccentric Vase', 45);

/* insert environments */
INSERT INTO `Environment` (`env_name`, `env_desc`, `stage`) VALUES ('Distant Roost', 'The Distant Roost is a bleak, dreary mountain region.', 1);
INSERT INTO `Environment` (`env_name`, `env_desc`, `stage`) VALUES ('Titanic Plains', 'The Titanic Plains are a vast, fractured, grassy plateau.', 1);
INSERT INTO `Environment` (`env_name`, `env_desc`, `stage`) VALUES ('Abandoned Aqueduct', 'The Abandoned Aqueduct is an arid, sprawling desert.', 2);
INSERT INTO `Environment` (`env_name`, `env_desc`, `stage`) VALUES ('Wetland Aspect', 'The Wetland Aspect is a moist mire consisting mostly of ruined stone structures and swampy areas filled with water.', 2);
INSERT INTO `Environment` (`env_name`, `env_desc`, `stage`) VALUES ('Rallypoint Delta', 'Rallypoint Delta is a desolate tundra.', 3);
INSERT INTO `Environment` (`env_name`, `env_desc`, `stage`) VALUES ('Scorched Acres', 'Large, circular platforms make up the majority of the stage, and embers float through the air.', 3);
INSERT INTO `Environment` (`env_name`, `env_desc`, `stage`) VALUES ('Abyssal Depths', 'The Abyssal Depths features a hellfire-forged zone of blazing heat', 4);
INSERT INTO `Environment` (`env_name`, `env_desc`, `stage`) VALUES ('Sundered Grove', 'The Sundered Grove is a dense, floral, jungle stage', 4);
INSERT INTO `Environment` (`env_name`, `env_desc`, `stage`) VALUES ('Sky Meadow', 'Sky Meadow is located within the upper atmosphere of Petrichor V', 5);
INSERT INTO `Environment` (`env_name`, `env_desc`, `stage`) VALUES ('Commencement', 'Commencement is the final stage and is located on the moon.', 6);
INSERT INTO `Environment` (`env_name`, `env_desc`, `hidden`) VALUES ('A Moment, Whole', 'A Moment, Whole can be reached from A Moment, Fractured, by obliterating at the Obelisk while at least one player holds the Beads of Fealty.', true);
INSERT INTO `Environment` (`env_name`, `env_desc`, `hidden`) VALUES ('Void Fields', 'The Void Fields can only be accessed via the Null Portal, which is located in a hidden cave in the shaft beneath the Blue Portal in the Bazaar.', true);
INSERT INTO `Environment` (`env_name`, `env_desc`, `hidden`) VALUES ('Bazaar Between Time', 'The Bazaar Between Time can be accessed by entering a Blue Portal that appears next to the Teleporter.', true);
INSERT INTO `Environment` (`env_name`, `env_desc`, `hidden`) VALUES ('Bulwark\'s Ambry', 'Bulwark\'s Ambry can be accessed by the Compound Generator in Sky Meadow.', true);

/* insert artificats */
INSERT INTO `Artifact` (`art_name`, `env_name`, `art_desc`, `unlock_pattern`) VALUES ('Artifact of Chaos', 'Abandoned Aqueduct', 'Friendly fire is enabled for both survivors and monsters alike.', 'Circle, Triangle, Circle; Circle, Triangle, Circle; Circle, Triangle, Circle');
INSERT INTO `Artifact` (`art_name`, `env_name`, `art_desc`, `unlock_pattern`) VALUES ('Artifact of Command', 'Bazaar Between Time', 'Choose your items.', 'Square, Square, Square; Square, Square, Square; Triangle, Triangle, Triangle');
INSERT INTO `Artifact` (`art_name`, `env_name`, `art_desc`, `unlock_pattern`) VALUES ('Artifact of Death', 'Wetland Aspect', 'When one player dies, everyone dies. Enable only if you want to truly put your teamwork and individual skill to the ultimate test.', 'Triangle, Circle, Triangle; Circle, Circle, Circle; Triangle, Circle, Triangle');
INSERT INTO `Artifact` (`art_name`, `env_name`, `art_desc`, `unlock_pattern`) VALUES ('Artifact of Dissonance', 'Abyssal Depths', 'Monsters can appear outside their usual environments.', 'Circle, Square, Square; Square, Square, Square; Square, Square, Circle');
INSERT INTO `Artifact` (`art_name`, `env_name`, `art_desc`, `unlock_pattern`) VALUES ('Artifact of Enigma', 'Bulwark\'s Ambry', 'Spawn with a random equipment that changes every time it\'s activated.', 'Diamond, Square, Square; Triangle, Square, Triangle; Circle, Diamond, Diamond');

/* insert monsters - regular */
INSERT INTO `Monster` (`mons_name`, `mons_health`, `mons_damage`, `mons_speed`, `mons_type`) VALUES ('Alloy Vulture', 140, 15, 3, 'Regular');
INSERT INTO `Monster` (`mons_name`, `mons_health`, `mons_damage`, `mons_speed`, `mons_type`) VALUES ('Beetle', 80, 12, 6, 'Regular');
INSERT INTO `Monster` (`mons_name`, `mons_health`, `mons_damage`, `mons_armor`, `mons_speed`, `mons_type`) VALUES ('Void Reaver', 1900, 12, 10, 6, 'Regular');
/* insert monsters - boss */
INSERT INTO `Monster` (`mons_name`, `mons_health`, `mons_damage`, `mons_armor`, `mons_speed`, `mons_type`) VALUES ('Beetle Queen', 2100, 25, 20, 6, 'Boss');
INSERT INTO `Monster` (`mons_name`, `mons_health`, `mons_regen`, `mons_damage`, `mons_armor`, `mons_speed`, `mons_type`) VALUES ('Scavenger', 3800, 2, 4, 20, 3, 'Boss');
INSERT INTO `Monster` (`mons_name`, `mons_health`, `mons_damage`, `mons_armor`, `mons_speed`, `mons_type`) VALUES ('Wandering Vagrant', 2100, 6.5, 15, 6, 'Boss');
/* insert monsters - special boss */
INSERT INTO `Monster` (`mons_name`, `mons_health`, `mons_damage`, `mons_armor`, `mons_speed`, `mons_type`) VALUES ('Alloy Worship Unit', 2500, 15, 30, 7, 'Special Boss');
INSERT INTO `Monster` (`mons_name`, `mons_health`, `mons_damage`, `mons_armor`, `mons_speed`, `mons_type`) VALUES ('Aurelionite', 2100, 40, 20, 5, 'Special Boss');
INSERT INTO `Monster` (`mons_name`, `mons_health`, `mons_damage`, `mons_armor`, `mons_speed`, `mons_type`) VALUES ('Mithrix', 1400, 16, 20, 15, 'Special Boss');
/* insert monsters - other */
INSERT INTO `Monster` (`mons_name`, `mons_health`, `mons_damage`, `mons_armor`, `mons_speed`, `mons_type`) VALUES ('Aurelionite (Ally)', 2100, 40, 20, 5, 'Other');
INSERT INTO `Monster` (`mons_name`, `mons_health`, `mons_regen`, `mons_damage`, `mons_speed`, `mons_type`) VALUES ('Beetle Guard (Ally)', 960, 1.5, 48, 17, 'Other');
INSERT INTO `Monster` (`mons_name`, `mons_health`, `mons_damage`, `mons_armor`, `mons_type`) VALUES ('Malachite Urchin', 250, 18, 100, 'Other');