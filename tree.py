import json
import copy


class FilterDict():
	def __init__(self, input_dict):
		self.input_dict = input_dict
		self.filter_dict = copy.deepcopy(self.input_dict)


	def filter(self, criteria, mod=0):
		keys = []
		for key, value in self.filter_dict.items():
			if (not criteria(value))^mod:
					keys.append(key)

		for key in keys:
			self.filter_dict.pop(key)


with open("db.json", "r") as jfile:
	db = json.load(jfile)


user_db = FilterDict(copy.deepcopy(db))

ans = {
	"ans":"1) Ваша передбачувана сума, витрачена на безпровідні навушники, перевищує 3000 грн",
	"condition":lambda x, : x["cost"] > 3000,
	"list":{
		0:{
			"ans":"2) Чи розглядаєте варіант безпровідних навушників з'єднаних між собою дротом? (ТИП наушників)",
			"condition":lambda x, : x["have_wire"],
			"list":{
				0:{
					"ans":"3) Можливість працювати кожному навушнику окремо",
					"condition":lambda x, : x["one_g"],
					"list":{
						0:{
							"end":True
						},
						1:{
							"ans":"4) Ємність батареї розрахована на роботу більше двох годин",
							"condition":lambda x, : x["capacity"],
							"list":{
								0:{
									"end":True
								},
								1:{
									"end":True
								}
							},
							"end":False
						}
					},
					"end":False
				},
				1:{
					"end":True
				}
			},
			"end":False
		},
		1:{
			"ans":"2) Вас цікавлять повнорозмірні накладні навушники",
			"condition":lambda x, : x["ower_ear"],
			"list":{
				0:{
					"ans":"3) Чи розглядаєте лише вакуумні безпровідні навушники? (Затички)",
					"condition":lambda x, : x["vacuum"],
					"list":{
						0:{
							"end":True
						},
						1:{
							"ans":"4) Навушники повинні володіти функцією шумопоглинання?",
							"condition":lambda x: x["down_noise"],
							"list":{
								0:{
									"end":True
								},
								1:{
									"ans":"5) Форма наушників повинна бути компактною? (без ніжки)",
									"condition":lambda x: x["compact"],
									"list":{
										0:{
											"end":True
										},
										1:{
											"end":True
										}
									},
									"end":False
								}
							},
							"end":False
						}
					},
					"end":False
				},
				1:{
					"ans":"3) Накладні безпровідні навушники обов'язково повинні складатися?",
					"condition":lambda x: x["folding"],
					"list":{
						0:{
							"end":True
						},
						1:{
							"ans":"4) Навушники повинні володіти функцією шумопоглинання?",
							"condition":lambda x: x["down_noise"],
							"list":{
								0:{
									"end":True
								},
								1:{
									"end":True
								}
							},
							"end":False
						}
					},
					"end":False
				}
			},
			"end":False
		}
	},
	"end":False
}

curent_ans = ""

while "end" in ans.keys() and not ans["end"]:
	cmd = input(f'{ans["ans"]} (yes/no)')
	curent_ans += f"{cmd}, "
	if cmd in ['yes', 'no']:
		if cmd == 'no':
			user_db.filter(ans["condition"], 1)
			ans = ans["list"][0]
		else:
			user_db.filter(ans["condition"])
			ans = ans["list"][1]


print(curent_ans)
print("Вам подойдут наушники:")
for k, v in user_db.filter_dict.items():
	print(f'\t{k}\n\tcost - {v["cost"]}')