article = "Among the many transitions that Queen Elizabeth II’s death has set in motion for Britain will be one that affects the smallest, and perhaps cutest, members of the royal family: the monarch’s pack of four royal dogs. These include two corgis, a corgi-dachshund cross (known as a dorgi) and a cocker spaniel.Buckingham Palace did not respond to a request for comment about who would be now caring for the dogs, named Candy, Lissy, Muick and Sandy. But wherever the royal canines end up, they may need to become accustomed to a home that is less luxurious than a castle. Charles, who will officially be proclaimed king on Saturday, reportedly prefers Jack Russell terriers over Pembroke Welsh corgis.The queen had more than 30 dogs, many of them corgis, during her seven-decade reign. But corgis do not have a long royal history — Elizabeth and her sister, Margaret, became the first people in the royal family to have one when, while they were young princesses in 1933, King George VI, then the Duke of York, got them a puppy, named Dookie. Another corgi, Jane, joined the royal family soon after, until 1944, when she was hit by a car. For Elizabeth’s 18th birthday, she got another corgi, a two-month-old puppy named Sue, who became known as Susan."

substitutions = {
  "royal":"vampiric",
  "family":"clan",
  "Queen":"Sorceror",
  "puppy":"demogorgon",
  
}


for key, value in substitutions.items():
  article = article.replace(key, value)

print(article)
    