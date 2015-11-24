# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

__author__ = "Johanes Kalas, Carissa Ulibasa, Devi Apriliani S, Jovanka Helen, Reza Haznam"
             
class Player:
	warna = ''
	mataDadu = 0
	posisi = 0
	def __init__(self, warna):
		self.warna = warna
	def getWarna(self):
		return self.warna
	def setPosition(self,x):
		self.posisi = x
	def getPosition(self):
		return self.posisi

import random

class Dice:
	mataDadu = 0
	def __init__(self):
		self.mataDadu = 0
	def getMataDadu(self):
                self.mataDadu = random.randint(1,6)
                return self.mataDadu
