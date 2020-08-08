from random import choice, randint

need_free_day = choice([True, False])
kinda_need = choice([True, False])
not_in_the_mood = choice([True, False])
on_demand_days = randint(0, 10)

# set this to True or False with Boolean Logic and Conditionals!
calling_in_on_demand = None

if need_free_day and on_demand_days > 0:
    calling_in_on_demand = True
elif kinda_need and not_in_the_mood and on_demand_days > 0:
    calling_in_on_demand = True
else:
    calling_in_on_demand = False
