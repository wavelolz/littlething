install.packages("tidyverse")
install.packages("conflicted")
library(tidyverse)
library(conflicted)
conflict_prefer("select", "dplyr")
conflict_prefer("filter", "dplyr")
install.packages("nycflights13")
library(nycflights13)
df <- nycflights13::flights
arrange(df, arr_time)

# arrange the column 
d1 = arrange(df, desc(arr_delay)) 

# select specific columns
d2 = select(d1, arr_delay, everything()) # put "arr_delay" column at first and  everything else at behind
select(df, year:dep_delay) 
select(df, contains("time")) # select columns which names contain "time"

# create new column by old column
d3 = select(df, year:day, ends_with("delay"), distance, air_time)
mutate(d3, hour = air_time / 60, days = hour / 24)
transmute(d3, hour = air_time / 60, days = hour / 24) # retain newly created variable only

# grouping data and counting the simple statistics
d4 = group_by(df, month)
summarize(d4, dep_time_mean = mean(dep_time, na.rm = T))


# pipe: combining multiple steps
d5 = group_by(df, dest)
d6 = summarize(d5, count = n(), ave_dist = mean(distance, na.rm = T), ave_delay = mean(arr_delay, na.rm = T))

d7 = df %>% group_by(dest) %>% 
  summarize(count = n(), 
            ave_dist = mean(distance, na.rm = T), 
            ave_delay = mean(arr_delay, na.rm = T)) %>% 
  filter(count > 20, dest != "NHL")

conflict_prefer("lag", "dplyr")
conflict_prefer("filter", "dplyr")
glimpse(mpg)
install.packages("patchwork")
library(patchwork)


# create plot using ggplot

# change color according to class
ggplot(mpg, aes(x = displ, y = hwy, color = class)) +
  geom_point()

# change color
ggplot(mpg, aes(x = displ, y = hwy)) +
  geom_point(color = "green")

# different kind of plot
ggplot(mpg, aes(x = class)) +
  geom_bar(color = "green")

ggplot(mpg, aes(x = displ, y = hwy)) +
  geom_line(color = "green") +
  geom_point(color = "red") +
  geom_smooth(color = "blue")

ggplot(mpg, aes(y = class)) +
  geom_bar()

ggplot(mpg, aes(x = displ, y = hwy)) +
  geom_point(aes(color = class)) +
  geom_smooth(se = FALSE)

mpg %>% ggplot(aes(x = class)) +
  geom_bar()

mpg %>% ggplot(aes(x = class, fill = drv)) +
  geom_bar(position = "fill") +
  scale_y_continuous(labels = scales::percent)

mpg %>% ggplot(aes(x = class, fill = drv)) +
  geom_bar(position = "dodge")

# plot by plotly 
install.packages("plotly")
library(plotly)
p1 <- mpg %>% ggplot(aes(x = displ, y = hwy, color = class)) +
  geom_point() +
  scale_color_brewer(palette = "Set1") +
  labs(title = "This is title",
       subtitle = "This is subtitle",
       x = "This is xaxis label",
       y = "This is yaxis label",
       color = "This is color label")
ggplotly(p1)

# dataexploer
install.packages("DataExplorer")
library(DataExplorer)
insurance <- read_csv("https://raw.githubusercontent.com/Ying-Ju/R_Data_Analytics_Series_NTPU/main/insurance.csv")
glimpse(insurance)
plot_intro(insurance)
plot_missing(insurance)
plot_bar(insurance)
plot_bar(insurance, with = "charges")
plot_histogram(insurance)
create_report(insurance, output_file = "report.html", output_dir = "Desktop")

# fancy R Markdown presentation
install.packages("xaringanthemer")
library(xaringanthemer)
install.packages("xaringan")
install.packages("flexdashboard")
library(flexdashboard)
