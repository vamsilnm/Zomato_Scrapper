class Zomato_Wrapper():
	def __init__(self,data):
		self.data = data
		self.Wrapper()
	def Wrapper(self):
		for i in range(0,5):
			self.data['user_reviews'][i]['review']['title'] = self.data['user_reviews'][i]['review'].pop('rating_text')
			del self.data['user_reviews'][i]['review']['timestamp']
			del self.data['user_reviews'][i]['review']['rating_color']
			del self.data['user_reviews'][i]['review']['id']
			self.data['user_reviews'][i]['review']['text'] = self.data['user_reviews'][i]['review'].pop('review_text')
			self.data['user_reviews'][i]['review']['date'] = self.data['user_reviews'][i]['review'].pop('review_time_friendly')
			self.data['user_reviews'][i]['review']['promotes'] = self.data['user_reviews'][i]['review'].pop('likes')
			self.data['user_reviews'][i]['review']['comments'] = self.data['user_reviews'][i]['review'].pop('comments_count')
			del self.data['user_reviews'][i]['review']['user']['foodie_color']
			del self.data['user_reviews'][i]['review']['user']['profile_image']
			del self.data['user_reviews'][i]['review']['user']['foodie_level']
			del self.data['user_reviews'][i]['review']['user']['profile_deeplink']
			self.data['user_reviews'][i]['review']['user']['url'] = self.data['user_reviews'][i]['review']['user'].pop('profile_url')
			self.data['user_reviews'][i]['review']['user']['followers_count'] = self.data['user_reviews'][i]['review']['user'].pop('foodie_level_num')
		self.data['reviews'] = self.data.pop('user_reviews')
		for i in range(0,5):
			self.data['reviews'][i] = self.data['reviews'][i].values()

