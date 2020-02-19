from PIL import Image
import pygame

raw_source_image = Image.open(r'imgs/collection.png')

# cropping sprites
player_walking_down_1 = raw_source_image.crop((0, 0, 18, 49))
player_walking_down_2 = raw_source_image.crop((20, 0, 38, 49))
player_walking_left_1 = raw_source_image.crop((40, 0, 58, 49))
player_walking_left_2 = raw_source_image.crop((60, 0, 81, 49))
player_walking_right_1 = player_walking_left_1.transpose(Image.FLIP_LEFT_RIGHT)
player_walking_right_2 = player_walking_left_2.transpose(Image.FLIP_LEFT_RIGHT)
player_walking_up_1 = raw_source_image.crop((140, 0, 158, 49))
player_walking_up_2 = player_walking_up_1.transpose(Image.FLIP_LEFT_RIGHT)
player_standing_down = raw_source_image.crop((83, 0, 103, 49))
player_standing_left = raw_source_image.crop((105, 0, 116, 49))
player_standing_right = player_standing_left.transpose(Image.FLIP_LEFT_RIGHT)
player_standing_up = raw_source_image.crop((118, 0, 138, 49))
floor_tile_1 = raw_source_image.crop((0, 51, 99, 150))
floor_tile_2 = raw_source_image.crop((101, 51, 200, 150))
floor_tile_3 = raw_source_image.crop((202, 51, 301, 150))
floor_tile_4 = raw_source_image.crop((303, 51, 402, 150))
wall_tile_1 = raw_source_image.crop((0, 152, 99, 251))


# pushing sprites into buffer
# DO NOT FORGET TO BUFFER CROPPED IMAGES!1!
buf_player_walking_down_1 = player_walking_down_1.tobytes()
buf_player_walking_down_2 = player_walking_down_2.tobytes()
buf_player_walking_left_1 = player_walking_left_1.tobytes()
buf_player_walking_left_2 = player_walking_left_2.tobytes()
buf_player_walking_right_1 = player_walking_right_1.tobytes()
buf_player_walking_right_2 = player_walking_right_2.tobytes()
buf_player_walking_up_1 = player_walking_up_1.tobytes()
buf_player_walking_up_2 = player_walking_up_2.tobytes()
buf_player_standing_down = player_standing_down.tobytes()
buf_player_standing_left = player_standing_left.tobytes()
buf_player_standing_right = player_standing_right.tobytes()
buf_player_standing_up = player_standing_up.tobytes()
buf_floor_tile_1 = floor_tile_1.tobytes()
buf_floor_tile_2 = floor_tile_2.tobytes()
buf_floor_tile_3 = floor_tile_3.tobytes()
buf_floor_tile_4 = floor_tile_4.tobytes()
buf_wall_tile_1 = wall_tile_1.tobytes()

# P.S. Also check the procedure of adding an image into pygame:
# pygame.image.fromstring(buf_, img.size, img.mode)
