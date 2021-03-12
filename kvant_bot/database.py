import sqlite3


class SQLighet:

	def __init__(self, database_file):
		self.connection = sqlite3.connect(database_file)
		self.cursor = self.connection.cursor()



	def get_subscriptions(self, rss = True):
		with self.connection:
			return self.cursor.execute("SELECT * FROM `users` WHERE 'rss' = ?", (rss,)).fetchall()


	def subscriber_exists(self, user_id):
		with self.connection:
			result = self.cursor.execute("SELECT * FROM `users` WHERE `user_id` = ?", (user_id,)).fetchall()
			return bool(len(result))


	def add_subscriber(self, user_id, rss = True):
		with self.connection:
			return self.cursor.execute("INSERT INTO `users` (`user_id`, `rss`) VALUES (?,?)", (user_id, rss))


	def update_subcritions(self,user_id,rss):
		return self.cursor.execute("UPDATE `users` SET `rss` = ? WHERE `user_id` = ?", (rss, user_id))


	def close(self):
		self.connection.close()