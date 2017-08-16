#author narumeena 
#description learning cobrrpy on antibiotic dataset 

from __future__ import print_function

import pprint as pp
import cobra
import cobra.test

# "ecoli" and "salmonella" are also valid arguments
model = cobra.test.create_test_model("textbook")


print(len(model.reactions))
print(len(model.metabolites))
print(len(model.genes))

pp.pprint(model.reactions[29])

pp.pprint(model.metabolites.get_by_id("atp_c")) 

pp.pprint(model) 