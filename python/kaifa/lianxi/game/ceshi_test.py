import unittest
from herostore import Hero


class TestHero(unittest.TestCase):
	def test_init_hero(self):
		xyb = Hero()
		xyb = Hero(name= 'xyb',hp=100,act=10)
		self.assertEqual(xyb.hp,100)
		self.assertEqual(xyb.act,10)
	
	def test_hero_say(self):
		hero = Hero(name= 'hero')
		hero.say()
		self.assertEqual(hero.hp,1000)
	
	def test_hero_go(self):

unittest.main()
