
# Accounting Python functions

class Accounting:
  
  # class attr
  book = "Financial Accounting"
  
  def hello(self):
    print("hello() says hello")








# ABC method
abc_costs = {
  'setting_up_machines': 300e3,
  'machining': 500e3,
  'inspecting': 100e3
}
cost_drivers = abc_costs.copy()
# add new dictionary keys and values to cost drivers dictionary
cost_drivers.update( {'expected_machine_setups': 1500} )
cost_drivers.update( {'expected_machine_hours': 50e3} )
cost_drivers.update( {'expected_inspections': 2000} )

def activity_overhead_rates(costing_data: dict):
  overhead_rates_1 = cost_drivers['setting_up_machines'] / cost_drivers['expected_machine_setups']
  overhead_rates_2 = cost_drivers['machining'] / cost_drivers['expected_machine_hours']
  overhead_rates_3 = cost_drivers['inspecting'] / cost_drivers['expected_inspections']
  
  print("\n --- Activity Based Overhead Rates --")
  print("per machine set up","."*8,"${:.2f}".format( overhead_rates_1))
  print("per machine hours","."*10,"${:.2f}".format( overhead_rates_2))
  print("per machine inpections","."*5,"${:.2f}".format( overhead_rates_3))
  

cost_drivers.update({'item_1': {'exp_cost_machine_setups':500, 'exp_cost_machining':30e3, 'exp_cost_inpsecting': 500} })
cost_drivers.update( {'item_2': {'exp_cost_machine_setups':1000, 'exp_cost_machining':20e3, 'exp_cost_inpsecting': 1500} })

# add the number of units produced, stated in the beginining of section
cost_drivers.update({'units_produced_item1': 25e3})
cost_drivers.update({'units_produced_item2': 5e3})

def product_overhead_costs( costing_data: dict ):
  # need rate for calculation
  overhead_rates_1 = cost_drivers['setting_up_machines'] / cost_drivers['expected_machine_setups'] # $200
  overhead_rates_2 = cost_drivers['machining'] / cost_drivers['expected_machine_hours']            # $10
  overhead_rates_3 = cost_drivers['inspecting'] / cost_drivers['expected_inspections']             # $50
  
  # -- item 1
  mach_setup_cost_1 = cost_drivers['item_1']['exp_cost_machine_setups'] * overhead_rates_1
  machine_cost_1 = cost_drivers['item_1']['exp_cost_machining'] * overhead_rates_2
  inspect_cost_1 = cost_drivers['item_1']['exp_cost_inpsecting'] * overhead_rates_3
  total_assigned_costs_1 = mach_setup_cost_1 + machine_cost_1 + inspect_cost_1
  overhead_cpu_1 = total_assigned_costs_1 / cost_drivers['units_produced_item1']
  
  #-- item 2
  mach_setup_cost_2 = cost_drivers['item_2']['exp_cost_machine_setups'] * overhead_rates_1
  machine_cost_2 = cost_drivers['item_2']['exp_cost_machining'] * overhead_rates_2
  inspect_cost_2 = cost_drivers['item_2']['exp_cost_inpsecting'] * overhead_rates_3
  total_assigned_costs_2 = mach_setup_cost_2 + machine_cost_2 + inspect_cost_2
  overhead_cpu_2 = total_assigned_costs_2 / cost_drivers['units_produced_item2']
  
  
  print("\n --- Product Overhead Costs ---")
  print("item 1")
  print("Cost assigned: machine set up ", "."*5,"${:,}".format(mach_setup_cost_1))
  print("Cost assigned: machine costs ", "."*6,"${:,}".format(machine_cost_1))
  print("Cost assigned: machine costs ", "."*6,"${:,}".format(inspect_cost_1))
  print("Total costs assigned","."*20,"${:,}".format(total_assigned_costs_1))
  print("Overhead cost per unit","."*18,"${:,}".format(overhead_cpu_1))
  print("item 2")
  print("Cost assigned: machine set up ", "."*5,"${:,}".format(mach_setup_cost_2))
  print("Cost assigned: machine costs ", "."*6,"${:,}".format(machine_cost_2))
  print("Cost assigned: machine costs ", "."*6,"${:,}".format(inspect_cost_2))
  print("Total costs assigned","."*20,"${:,}".format(total_assigned_costs_2))
  print("Overhead cost per unit","."*18,"${:,}".format(overhead_cpu_2))
  
high_vol_item = 25e3
low_vol_item = 5e3
expect_overhead = 900e3
hours = 1
# ------

total_annual_direct_labor = high_vol_item + low_vol_item

pred_overhead_rate = expect_overhead / total_annual_direct_labor
print("Predetermined overhead rate = $",pred_overhead_rate * hours)

manuf_costs = {
  'item_1': {'direct_material': 40, 'direct_labor': 12, 'overhead_rate': 30},
  'item_2': {'direct_material': 30, 'direct_labor': 12, 'overhead_rate': 30}
}

def unit_comparison( manufacturing_data: dict,  item_1_cpu: int, item_2_cpu: int):
  
  # convert the dictionary into a list
  m = list( manuf_costs )
  # create an empty array to loop through the values and sum them
  ml = []
  for x in m:
    sx = sum( manuf_costs[x].values() )
    ml.append(sx)  # append the summed values to the array
      
  print("Tradional costing")
  print("\titem 1 product total unit cost = $", ml[0])
  print("\titem 2 product total unit cost = $", ml[1])


  # item 1 overhead cost per unit
  # item_1_cpu = 17
  # item_2_cpu = 95
    
  abc_1 = (manuf_costs['item_1']['direct_material'] + manuf_costs['item_1']['direct_labor'] + item_1_cpu)
  abc_2 = (manuf_costs['item_2']['direct_material'] + manuf_costs['item_2']['direct_labor'] + item_2_cpu)
    
  print("ABC method")
  print("\titem 1 product total unit cost = $", abc_1 )
  print("\titem 2 product total unit cost = $", abc_2)
  
  
  
  
  








