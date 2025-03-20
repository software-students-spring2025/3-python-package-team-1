from src.ratpack.infest import infest, visualize_infestation, count_rats, exterminate

'''Function providing code examples for the ratpack package'''

@infest(infestation_level=3, rat_types=["sewer_rat", "brown_rat"])
def demo_fn():
    return 1+1

demo_fn()

print(count_rats())

visualization = visualize_infestation()
print(visualization)

extermination_statistics = exterminate(dry_run=True)

exterminate()