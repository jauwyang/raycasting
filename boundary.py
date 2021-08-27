from math_tools import Vector2D, distance
import math
import pygame
from config import WHITE, WINDOW_HEIGHT, WINDOW_WIDTH, FOV


class Boundary:
    def __init__(self, x1, y1, x2, y2):
        self.a = Vector2D(x1, y1)
        self.b = Vector2D(x2, y2)
    
    def draw(self, window):
        pygame.draw.line(window, WHITE, (self.a.x, self.a.y), (self.b.x, self.b.y),2)


class Ray:
    def __init__(self, pos, angle):
        self.pos = pos
        self.dir = Vector2D(math.cos(angle), math.sin(angle))  # direction is relative to the origin
        self.angle = angle

    def draw(self, window):
        pygame.draw.line(window, WHITE, (self.pos.x, self.pos.y), (self.pos.x + self.dir.x * 50, self.pos.y + self.dir.y * 50))

    def set_angle(self, angle):
        self.dir = Vector2D(math.cos(angle), math.sin(angle))

    def look_at(self, x, y):
        self.dir = Vector2D(x,y)

    def cast(self, wall):
        x1 = wall.a.x
        y1 = wall.a.y
        x2 = wall.b.x
        y2 = wall.b.y

        x3 = self.pos.x
        y3 = self.pos.y
        x4 = self.dir.x + self.pos.x
        y4 = self.dir.y + self.pos.y

        denom = (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4)
        if (denom == 0):
            return
        
        t = ((x1 - x3) * (y3 - y4) - (y1 - y3) * (x3 - x4)) / denom
        u = -((x1 - x2) * (y1 - y3) - (y1 - y2) * (x1 - x3)) / denom
        if (t > 0 and t < 1 and u > 0):
            x = x1 + t * (x2 - x1)
            y = y1 + t * (y2 - y1)
            pt = Vector2D(x, y)
            return pt
        else:
            return


class Particle:
    def __init__(self):
        self.pos = Vector2D(WINDOW_WIDTH / 4, WINDOW_HEIGHT / 2)
        self.rays = []
        self.heading = 0
        for angle in range(int(round(FOV) / -2), int(round(FOV) / 2)):
            self.rays.append(Ray(self.pos, math.radians(angle)))
    
    def rotate(self, angle):
        self.heading += angle
        offset = 0
        for ray in self.rays:
            ray.set_angle(math.radians(offset) + self.heading)
            offset += 1

    def draw(self, window):
        pygame.draw.circle(window, (255, 0, 0), (self.pos.x, self.pos.y), 3)

    def look(self, window, walls):
        scene = []
        for ray in self.rays:
            closest = None
            record = math.inf
            for wall in walls:
                pt = ray.cast(wall)
                if (pt is not None):
                    dist = distance(self.pos.x, self.pos.y, pt.x, pt.y)
                    # a = abs(ray.angle - self.heading)
                    # dist *= math.cos(a)
                    if (dist < record):
                        record = dist
                        closest = pt
            if closest is not None:
                pygame.draw.line(window,(255, 255, 255), (self.pos.x, self.pos.y), (closest.x, closest.y))
            scene.append(record)
        
        return scene