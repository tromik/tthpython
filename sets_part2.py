def sep():
    print("-" * 160)
    print("")
    print("-" * 160)

# union - combination of two or more sets, each item only once (no dupes/repeats)
# difference - everything in one set but not another
# symmetric difference - everything that is unique to all sets, no shared items
# intersection - a new set containing all items that are in both sets (the items
#                   that would not appear in the symmetric difference)

set1 = set(range(10))
set2 = {1, 2, 3, 5, 7, 11, 13, 17, 19, 23}

union_set = set1.union(set2)
print("union set: {}".format(union_set)) # --> union set: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 13, 17, 19, 23}
# note that set1.update(set2) would give the same result but not as a new set
# union() does not change any of the incoming sets

# another way to write the untion is with the | char
new_union_set = set1 | set2
print("piped union set: {}".format(union_set))
    # --> piped union set: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 13, 17, 19, 23}

sep()
# difference
set1_diff_set = set1.difference(set2)
print("diff set 1: {}".format(set1_diff_set))

set2_diff_set = set2.difference(set1)
print("diff set 2: {}".format(set2_diff_set))

# differences can also be done with a hyphen (-)
new_set1_diff_set = set1 - set2
print("diff set 1: {}".format(new_set1_diff_set))

new_set2_diff_set = set2 - set1
print("diff set 2: {}".format(new_set2_diff_set))

sep()
# symmetric difference
symm_diff = set1.symmetric_difference(set2)
print("symm diff: {}".format(symm_diff))

# this can also be done with the ^ character
new_symm_diff = set2 ^ set1
print("new symm diff: {}".format(new_symm_diff))

sep()
# intersection
inter_set = set1.intersection(set2)
print("inter set: {}".format(inter_set))

# this can also be done with the & character
new_inter_set = set1 & set2
print("new inter set: {}".format(new_inter_set))
