# CURL Commands to easily test both endpoints


curl -X POST http://localhost:34567/summarize \
-H "Content-Type: application/json" \
-d '{"text":"The orca (Orcinus orca), or killer whale, is a toothed whale that is the largest member of the oceanic dolphin family. It is the only extant species in the genus Orcinus. Orcas are recognizable by their black-and-white patterned body. A cosmopolitan species, orcas are found in diverse marine environments, from Arctic to Antarctic regions to tropical seas."}'

curl -X POST http://127.0.0.1:34567/summarize \
-H "Content-Type: application/json" \
-d '{"text":"The orca (Orcinus orca), or killer whale, is a toothed whale that is the largest member of the oceanic dolphin family. It is the only extant species in the genus Orcinus. Orcas are recognizable by their black-and-white patterned body. A cosmopolitan species, orcas are found in diverse marine environments, from Arctic to Antarctic regions to tropical seas."}'

curl -X POST http://localhost:34567/generate-questions \
-H "Content-Type: application/json" \
-d '{"text":"Penguins live almost exclusively in the Southern Hemisphere: only one species, the Galápagos penguin, is found north of the Equator. Highly adapted for life in the ocean water, penguins have countershaded dark and white plumage and flippers for swimming. Most penguins feed on krill, fish, squid and other forms of sea life which they catch with their bills and swallow whole while swimming. A penguin has a spiny tongue and powerful jaws to grip slippery prey."}'
