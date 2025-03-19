from ratpack import infest, visualize_infestation, count_rats, exterminate

'''Function providing code examples for the ratpack package'''

@infest(infestation_level=4)
def demo_fn():
    return 1+1

demo_fn()

print(count_rats())

visualization = visualize_infestation()

extermination_statistics = exterminate(dry_run=True)

exterminate()