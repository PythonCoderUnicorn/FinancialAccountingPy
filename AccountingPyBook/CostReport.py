



  

  
  #-----------------------------------------------------
  def physical_flow(cost_data= list):
  
    # units to be accounted for = wip_start + started_transferred
    tot_units = mixing_data[0]['units']['wip_start'] + mixing_data[0]['units']['units_in_production']
  
    # units accounted for = completed_transferred + wip_end
    units_acc = mixing_data[0]['units']['units_completed_transferred'] + mixing_data[0]['units']['wip_end']
  
    print("-- Physical Unit Flow --")
    print("Total units accounted for  ","."*5,"{:,}".format(tot_units))
    print("Total units   ", "."*18,"{:,}".format(tot_units))
  #-----------------------------------------------------
  
  
  #-----------------------------------------------------
  def equivalent_units(cost_data= list):
    materials_equiv_cost = (mixing_data[0]['units']['wip_end'] * mixing_data[0]['units']['wip_end_materials_percent']) + mixing_data[0]['units']['units_completed_transferred']
  
    conv_costs_equiv_cost = (mixing_data[0]['units']['wip_end'] * mixing_data[0]['units']['wip_end_conversion_costs_percent']) + mixing_data[0]['units']['units_completed_transferred']

    print("-- Equivalent Units --")
    print("Equivalent units (materials) = ","."*12,"{:,}".format(materials_equiv_cost))
    print("Equivalent units (conversion costs) = ","."*5,"{:,}".format(conv_costs_equiv_cost))
  #-----------------------------------------------------
  
  
  
  
  
  
def production_costs( cost_data= list):
  
    materials_equiv_cost = (mixing_data[0]['units']['wip_end'] * \
      mixing_data[0]['units']['wip_end_materials_percent']) + \
      mixing_data[0]['units']['units_completed_transferred']
    
    tot_material_cost = mixing_data[1]['costs']['wip_start_direct_materials'] +\
      mixing_data[1]['costs']['costs_direct_materials']
    
    unit_material_cost = tot_material_cost / materials_equiv_cost
    
    tot_conv_cost = mixing_data[1]['costs']['wip_start_conversion_costs'] + \
      mixing_data[1]['costs']['costs_conversion_costs']
    
    conv_costs_equiv_cost = (mixing_data[0]['units']['wip_end'] *\
      mixing_data[0]['units']['wip_end_conversion_costs_percent']) +\
      mixing_data[0]['units']['units_completed_transferred']
    
    unit_conv_cost = tot_conv_cost / conv_costs_equiv_cost
    
    tot_manuf_cpu = unit_material_cost + unit_conv_cost
    
    transf_out = mixing_data[0]['units']['units_completed_transferred'] * \
      tot_manuf_cpu
      
    tot_cost_recon = (mixing_data[0]['units']['wip_end'] * \
      unit_material_cost) + ((mixing_data[0]['units']['wip_end'] * \
      mixing_data[0]['units']['wip_end_conversion_costs_percent']) *\
      unit_conv_cost)
    
    recon_sched = transf_out + tot_cost_recon
    
    print("-- Unit Production Costs --")
    print("Total materials costs  ","."*15,"${:,}".format(tot_material_cost))
    print("Unit materials cost  ","."*17,"${:,}\n".format(unit_material_cost))
    
    print("Total conversion costs ","."*15,"${:,}".format(tot_conv_cost))
    print("Unit conversion costs  ","."*17,"${:,}".format(unit_conv_cost))
    print("Total manufacturing cost per unit  ","."*5,"${:,}\n".format(tot_manuf_cpu))
    
    print("Cost reconciliation schedule  ","."*5,"${:,}".format(recon_sched))
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
