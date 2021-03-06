import discord 
import asyncio
import random
from discord.ext import commands
import os
import datetime
import pymongo
import json
import math
db_client=pymongo.MongoClient(os.getenv("DB_URL"))
db1_client=pymongo.MongoClient(os.getenv("DB2_URL"))

class set(commands.Cog):
	def __init__(self,bot):
        	self.bot=bot
	@commands.command(aliases=["change_about"])
	@commands.guild_only()
	async def set(self,ctx,key=None,*,about=None):
		if key==None:
			return
		if key.lower()!="about":
			return
		if about==None:
			return
		x=db2_collection.find_one({"id":ctx.message.author.id})
		if x==None:
			return
		else:
			db2_collection.update_one({"id":ctx.author.id},{"$set":{"about":about}})
			await ctx.send(f"Changed your about to '{about}'")

def setup(bot):
	bot.add_cog(set(bot))
