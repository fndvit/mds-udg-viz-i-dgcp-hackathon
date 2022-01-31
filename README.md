# Hackathon Infoviz and Project Management

![License](https://img.shields.io/github/license/fndvit/mds-udg-viz-i-dgcp-hackathon?style=for-the-badge) ![Issues](https://img.shields.io/github/issues/fndvit/mds-udg-viz-i-dgcp-hackathon?style=for-the-badge) 

## Project background

This project is part of a country by country view of climate change metrics. Among those metrics *(depending on data availability and relevance for the country)* are:

* GHG emissions: latest, per capita, and trend since 1970
* Latest land surface temperature anomalies
* Latest sea surface temperature *(where relevant)* 👈 **OUR FOCUS**
* Climate risk index
* Detailed net-zero targets *(regional and city-level data where available)*
* And about half a dozen more

> **⚠ IMPORTANT NOTE:**  
> **Again, our focus for this hackathon** is *ONLY* the **'Latest sea surface temperature'** metric!

The overall project will be part of a series which includes [this interactive](https://www.unep.org/explore-topics/climate-action/what-we-do/climate-action-note/state-of-climate.html):

[![Screenshot of the interactive](preview-climate-change.png)](https://www.unep.org/explore-topics/climate-action/what-we-do/climate-action-note/state-of-climate.html "Climate Action Note")

## Some context about the raw data: Sea surface temperature

NASA's sea surface temperature product shows the temperature of the top millimeter of the ocean's surface. Scientists monitor sea surface temperature because the ocean's warmth influences Earth's climate system in many different ways. The Moderate Resolution Imaging Spectroradiometer (MODIS) instruments aboard NASA's Terra and Aqua satellites collect global measurements of sea surface temperature accurate to within half a degree Celsius.

Here're [more detailed explanations](https://neo.gsfc.nasa.gov/view.php?datasetId=MYD28M).

You can find the data starting Jan. 2012 as `gzipped CSVs` in [`./data/raw/SST-CSVs`](data/raw/SST-CSVs)

And in different formats here going back to 2002:

* As [`PNGs`](https://neo.gsfc.nasa.gov/archive/rgb/MYD28M/)
* As [`GEOTIFFs`](https://neo.gsfc.nasa.gov/archive/geotiff/MYD28M/)

It looks like this projected using Equal Earth projection [![Sea surface temperature](https://interactives.unenvironment.org/explore-topics/climate-action/what-we-do/climate-action-note/ocean.jpg)]

## Scenarios and objectives

### From observations to anomalies

|:------|
|**Team name:** gerbils 🐹|
|:------|
|**Members:** Cédric, Esther, Marc Pérez, Àlex|

**Question:** How can we create Sea Surface Temperature Anomaly maps off the Sea Surface Temperature data?

**Context:** NASA used to have Sea Surface Temperature Anomaly data, from a different instrument, but it ended data collection in October 2011 due to problems with the rotation of its antenna.

As a starting point, you could investigate this similar product: the [Land Surface Temperature Anomaly page](https://neo.gsfc.nasa.gov/view.php?datasetId=MOD_LSTAD_M)— in the product page it says:
> These maps show where Earth’s surface was warmer or cooler in the daytime than the average temperatures for the same week or month from 2001-2010. So, a land surface temperature anomaly map for May 2002 shows how that month’s average temperature was different from the average temperature for all Mays between 2001 and 2010.

**Deliverables:**

### Areas of interest

|:------|
|**Team name:** koalas 🐨|
|:------|
|**Members:** Andrea, Daniel, Marc Rojo, Pau|

**Question:** How do we find any statistically significant clustering in the spatial patterns of this data?

**Context:** You don't have the sea surface temperature anomalies yet —team gerbils 🐹 is working on that— but both the [Land Surface Temperature Anomaly page](https://neo.gsfc.nasa.gov/view.php?datasetId=MOD_LSTAD_M) and the original [Sea Surface Temperature Anomaly](https://neo.gsfc.nasa.gov/view.php?datasetId=AMSRE_SSTAn_M) can serve as starting points.

**Deliverables:**

### TK TK

|:------|
|**Team name:** badgers 🦡|
|:------|
|**Members:** Sergi, Jonah, Victor, Guillem|



## Day-of schedule

* 👋 09:00 Welcome, reminder of logistics like lunch, drinks, communication channels ...
* 🙋‍♀️ 09:15 Standup meeting with us. Objectives, processes, what you want to achieve in the hackathon and any questions.
* 👩‍💻 09:30 Start of work day!
* 🙋‍♀️ 13:15 Short standup
* 🍱 13:30 Lunch
* 👩‍💻 14:30 Back to work, switch PMs
* 🧑‍🏫 19:00 Wrap-up presentation < 6 slides 😜: About 5-10 minutes per team.
  * What was achieved?
  * What was helpful?
  * What’s left to do?
* 🏆 19:30 Awards
* 🥳 20:00 End!!!

*We'll come to you, moving from group to group, and we'll be available for questions and solving blocks.*

## Collaboration recommendations

* Follow the Branch Per Feature model: one feature, one branch.
* Prepend each branch with your team name. For example if you're commiting part of your work cleaning up the data, you would push it to a `gerbils--data-cleaning` branch.
* Use a consistent pattern for commit messages, a nice one is `type: subject` as in `refactor: use map instead of for loop`.

## The awards

As we all know the [professional jury and the popular vote don't always match](https://www.youtube.com/watch?v=4uGN9efcACw), so we're offering two awards: you all decide one via an open vote, we decide the other —which may or may not be the same, and we won't know until we reveal them simultaneously.

* 🏆 **Popular vote**
* 🏆 **Jury fav**
