# imports
import os
import csv
import sys
import lazyqsar

# parse arguments
input_file = sys.argv[1]
output_file = sys.argv[2]

# current file directory
root = os.path.dirname(os.path.abspath(__file__))

MODELPATH = os.path.join(root, "..", "..", "checkpoints")
model_5um = os.path.join(MODELPATH, "ic50_hepg2_72h_5uM")
model_10um = os.path.join(MODELPATH, "ic50_hepg2_72h_10uM")

# my model
def predict(smiles, model_dir):
    print(f"Length of the X sample: {len(smiles)}")
    model = lazyqsar.LazyBinaryClassifier.load_model(model_dir)
    chemeleon = lazyqsar.descriptors.ChemeleonDescriptor()
    X = chemeleon.transform(smiles)
    y_hat = model.predict_proba(X=X)[:,1]
    return y_hat

# read SMILES from .csv file, assuming one column with header
with open(input_file, "r") as f:
    reader = csv.reader(f)
    next(reader)  # skip header
    smiles_list = [r[0] for r in reader]

# run model
output1 = predict(smiles_list, model_5um)
output2 = predict(smiles_list, model_10um)


# write output in a .csv file
with open(output_file, "w") as f:
    writer = csv.writer(f)
    writer.writerow(["HepG2_IC50_72h_5uM".lower(), "HepG2_IC50_72h_10uM".lower()])
    for o1, o2, in zip(output1, output2):
        writer.writerow([o1, o2])
