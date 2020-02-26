######################
# Create your own ggplot2 theme or see ggthemes package
# https://cran.r-project.org/web/packages/ggthemes/vignettes/ggthemes.html
# http://sape.inf.usi.ch/quick-reference/ggplot2/themes
# The following is modified from:
# https://stackoverflow.com/questions/31404433/is-there-an-elegant-way-of-having-uniform-font-size-for-the-whole-plot-in-ggplot
# If re-using functions it is much better to copy this to a new script and run here as:
# source('my_ggplot_theme.R')

# A4 paper measures 210 x 297 millimeters or 8.27 x 11.69 inches
######################

######################
theme_my <- function(base_size = 11, base_family = "Times") {
  normal_text <- element_text(size = as.numeric(base_size), colour = "black", face = "plain")
  large_text <- element_text(size = as.numeric(base_size + 1), colour = "black", face = "plain")
  bold_text <- element_text(size = as.numeric(base_size + 1), colour = "black", face = "bold")
  axis_text <- element_text(size = as.numeric(base_size - 1), colour = "black", face = "plain")
  theme_classic(base_size = base_size, base_family = base_family) +
    theme(legend.key = element_blank(),
          strip.background = element_blank(),
          text = normal_text,
          plot.title = bold_text,
          axis.title = large_text,
          axis.text = axis_text,
          legend.title = bold_text,
          legend.text = normal_text,
          plot.margin = unit(c(3, 5, 2, 2),"mm") #t, r, b, l
          # plot.margin = grid::unit(c(1,1,1,1), "mm") 
          )
  }
# theme_my()
######################

######################
# The following is modified from:
# https://rpubs.com/Koundy/71792
library(scales)
library(grid)
library(ggthemes)

theme_Publication <- function(base_size = 13, base_family = "Times") {
  # library(grid)
  # library(ggthemes)
  (theme_foundation(base_size = base_size, base_family = base_family)
    + theme(plot.title = element_text(face = "bold",
                                      size = rel(1.2), hjust = 0.5),
            text = element_text(),
            panel.background = element_rect(colour = NA),
            plot.background = element_rect(colour = NA),
            panel.border = element_rect(colour = NA),
            axis.title = element_text(face = "bold", size = rel(1)),
            axis.title.y = element_text(angle = 90, vjust = 2),
            axis.title.x = element_text(vjust = -0.2),
            axis.text = element_text(),
            axis.line = element_line(colour = "black"),
            axis.ticks = element_line(),
            # panel.grid.major = element_line(colour = "#f0f0f0"),
            panel.grid.major = element_blank(),
            panel.grid.minor = element_blank(),
            # legend.key = element_rect(fill = "white", colour = " light grey"),
            legend.key = element_rect(colour = NA),
            # legend.position = "bottom",
            # legend.direction = "horizontal",
            legend.key.size = unit(0.5, "cm"),
            # legend.key.width = unit(0.2, "cm"),
            # legend.margin = margin(0, 0, 0, 0),
            # legend.title = element_text(face = "italic"),
            # plot.margin = unit(c(10, 5, 5, 5),"mm"),
            # plot.margin = unit(c(3, 5, 2, 2), "mm"), #t, r, b, l
            strip.background = element_rect(colour = "#f0f0f0", fill = "#f0f0f0"),
            strip.text = element_text(face = "bold")
    ))
}

scale_fill_Publication <- function(...){
  # library(scales)
  discrete_scale("fill", "Publication", 
                 manual_pal(values = c("#386cb0",
                                       "#fdb462",
                                       "#7fc97f",
                                       "#ef3b2c",
                                       "#662506",
                                       "#a6cee3",
                                       "#fb9a99",
                                       "#984ea3",
                                       "#ffff33")),
                 ...)
  
}

scale_colour_Publication <- function(...){
  # library(scales)
  discrete_scale("colour", "Publication",
                 manual_pal(values = c("#386cb0",
                                       "#fdb462",
                                       "#7fc97f",
                                       "#ef3b2c",
                                       "#662506",
                                       "#a6cee3",
                                       "#fb9a99",
                                       "#984ea3",
                                       "#ffff33")),
                 ...)
  
}
######################