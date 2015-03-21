Private Event Log REST Service
==============================

This is simple REST API made in django with django rest framework.

It consumes events in the form of a string "I just win a lottery #update @all"
parses them to JSON and it's possible to get events by category ('#update'),
by person ('@all') or by time.
