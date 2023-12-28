#3C) Усложнение 2Л. Теперь события могут пересекаться.
# Если пересекаются два события - все нормально. Если три и более - говорим, что нельзя добавить в список событий.

class Event:
    def __init__(self, start, stop):
        self.start = start
        self.stop = stop


class EventList:
    def __init__(self):
        self.events = []

    def add(self, event: Event):
        intersections = self.getIntersections(event)
        if len(intersections) < 3:
            self.events.append(event)
            return True
        return False

    def getIntersections(self, new_event):
        intersections = []
        openedEvents = set()
        currentIntersection = []

        sequence = self.createEventSequence(new_event)
        intersections.append(currentIntersection)

        for i in range(len(sequence)):
            event = sequence[i]['event']
            if event in openedEvents:
                openedEvents.remove(event)
                if len(openedEvents) == 0 and i != len(sequence) - 1:
                    currentIntersection = []
                    intersections.append(currentIntersection)
                continue

            openedEvents.add(event)
            currentIntersection.append(event)

        for events in intersections:
            if new_event in events:
                return events

        return [new_event]

    def createEventSequence(self, new_event):
        sequence = [{'event': new_event, 'time': new_event.start}, {'event': new_event, 'time': new_event.stop}]

        for event in self.events:
            sequence.append({'event': event, 'time': event.start})
            sequence.append({'event': event, 'time': event.stop})

        sequence.sort(key=lambda e: e['time'])
        return sequence


event_list = EventList()

print(event_list.add(Event(5, 10)))
print(event_list.add(Event(11, 15)))
print(event_list.add(Event(7, 9)))
print(event_list.add(Event(8, 20)))
