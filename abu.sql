BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS `music` (
	`file_id`	TEXT NOT NULL UNIQUE,
	`right_answer`	TEXT NOT NULL,
	`wrong_answers`	TEXT NOT NULL,
	`id`	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE
);
INSERT INTO `music` VALUES ('AwADAgAD3QEAAs7XKUiAckxpJ-XbqwI','ABBA – Lay All Your Love on Me','Boney M. - Daddy Cool,Bee Gees – Stayin’ Alive,Kylie Minogue – Can’t Get You Out of My Head,Carpenters – Close to You',1);
INSERT INTO `music` VALUES ('AwADAgAD3gEAAs7XKUhuaqHPIl2exAI','Kings of Leon – Sex on Fire','The Killers – Mr. Brightside,The Strokes – Last Nite,Kasabian – You’re In Love With a Psycho,Arctic Monkeys – Arabella',2);
INSERT INTO `music` VALUES ('AwADAgAD4AEAAs7XKUgyA0yOqkJz9wI','Ed Sheeran – Photograph','Passenger – Get Off The Rails,Shawn Mendes – There’s Nothing Holding Me Back,James Arthur – Say You Won’t Let Go,One Direction – Drag Me Down',3);
INSERT INTO `music` VALUES ('AwADAgAD4QEAAs7XKUjb3bzXU5630gI','Coldplay – The Scientist','Keane – Love Is The End,Snow Patrol – Chasing Cars,Imagine Dragons – It’s Time,Fray – You Found Me',4);
INSERT INTO `music` VALUES ('AwADAgAD4gEAAs7XKUhpGQJ82E6M3gI','Elvis Presley – Can’t Help Falling in Love','Jerry Lee Lewis – Great Balls of Fire,Chuck Berry – Carol,Frank Sinatra – Fly Me To The Moon,Louis Armstrong – Summertime',5);
INSERT INTO `music` VALUES ('AwADAgAD4wEAAs7XKUhrxslIPzMrKAI','Eric Clapton – Tears in Heaven','Derek and the Dominos – Layla,Joe Bonamassa – Drive,Mark Knopfler – What It Is,B.B.King – Hummingbird',6);
INSERT INTO `music` VALUES ('AwADAgAD5AEAAs7XKUjQBJq0LpHhpgI','Edith Piaf – Sous le ciel de Paris','Marlene Dietrich – Lili marleen,Carla Bruni – French Touch,Juliette Greco – Les feuilles mortes,Zaz – Les passants',7);
INSERT INTO `music` VALUES ('AwADAgAD5QEAAs7XKUjcstVEiojU9AI','Andrea Bocelli – Moon River','Andy Wiiliams – Breakfast at Tiffany,Josh Groban – You Raise Me Up,Luciano Pavarotti – Forever,Frank Sinatra – Fly Me To The Moon',8);
INSERT INTO `music` VALUES ('AwADAgAD5gEAAs7XKUjggR1lGSMDmgI','of Monsters and Men – Love Love Love','The Lumineers – Stubborn Love,Mumford & Sons – Little Lion Man,Vance Joy – Mess Is Mine,Florence + the Machine – Delilah',9);
INSERT INTO `music` VALUES ('AwADAgAD6AEAAs7XKUgSXFBhq5vpUQI','Drake – Hotline Bling','Future – Feed Me Dope,Kanye West – Power,J.Cole – Power Trip,The Weeknd - Starboy',10);
COMMIT;
