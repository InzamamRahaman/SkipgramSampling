
from vocab import Vocabulary
from sampler import Sampler

corpus = """
The Georgia Institute of Technology (commonly referred to as Georgia Tech, Tech, or GT) is a public research university in Atlanta, Georgia, in the United States. It is a part of the University System of Georgia and has satellite campuses in Savannah, Georgia; Metz, France; Athlone, Ireland; Shenzhen, China; and Singapore.

The educational institution was founded in 1885 as the Georgia School of Technology as part of Reconstruction plans to build an industrial economy in the post-Civil War Southern United States. Initially, it offered only a degree in mechanical engineering. By 1901, its curriculum had expanded to include electrical, civil, and chemical engineering. In 1948, the school changed its name to reflect its evolution from a trade school to a larger and more capable technical institute and research university.
"""

content = corpus.split()
content = map(lambda x: x.lower(), content)
content = list(content)
sam = Sampler(content, 2)
print(sam.batch_sample())
