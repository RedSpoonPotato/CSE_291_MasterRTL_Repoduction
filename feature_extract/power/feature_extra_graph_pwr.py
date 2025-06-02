import numpy as np
import pickle, json, time, re
from DG import Graph

def run_one_design(design_name, cmd, out_path):
        with open(f"../../example/feature/{design_name}_{cmd}_vec_area.json", 'r') as f:
            feat_vec = json.load(f)

        with open(f"../../example/verilog/toggle_rate/{design_name}_tc_sum_all.json", 'r') as f:
            tr_sum = json.load(f)
            feat_vec.append(tr_sum)
        
        with open(f"../../example/verilog/toggle_rate/{design_name}_tc_avr_all.json", 'r') as f:
            tr_avr = json.load(f)
            feat_vec.append(tr_avr) 

        ### ---- load the prediction of module level power 'pred_pwr' ---- ###
        pred_pwr = 0
        ######################################################################

        feat_vec.append(pred_pwr)

        print(feat_vec)
        vec_name = out_path + f'/{design_name}_{cmd}_vec_pwr.json'
        with open(vec_name, 'w') as f:
                json.dump(feat_vec, f)
             
if __name__ == '__main__':

        # design_name = 'TinyRocket'
        top_modules = [
        # "s13207",
        # "s5378",
        # "s38584",
        # "s35932",
        # "s38417",
        "b10",
        "b11",
        "b12",
        "b13",
        "b14",
        "b15",
        # "b16",
        "b17",
        "b18",
        "b19",
        "b20",
        "b21",
        "b22",
        ]
        for design_name in top_modules:
            cmd = 'sog'
            out_path = "../../test/feature"
            run_one_design(design_name, cmd, out_path)