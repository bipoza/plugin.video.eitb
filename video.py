from utils import get_programs
from utils import get_episodes
from utils import get_videos
from utils import get_last_broadcast
from utils import get_programs_types
from utils import get_programs_types_playlist
import xbmcgui
import xbmcplugin
import xbmcaddon
# import xbmc
from constants import MENU_ITEMS

addon = xbmcaddon.Addon()

class VideoHandler(object):
    def __init__(self, handle, url):
        self.handle = handle
        self.url = url

    def list_menu(self):

        listing = []
        for item in MENU_ITEMS:
            title = item.get('title')
            option = item.get('@id')
            icon = item.get('icon')
            # Create a list item with a text label and a thumbnail image.
            list_item = xbmcgui.ListItem(label=title)
            list_item.setInfo('video', {'title': title})
            list_item.setArt({'icon': addon.getAddonInfo("path") + icon})
            url = '{0}?action=videomenu&option={1}'.format(self.url, option)
            is_folder = True
            listing.append((url, list_item, is_folder))

        # Set Content
        xbmcplugin.setContent(self.handle, 'tvshows')
        # Add our listing to Kodi.
        xbmcplugin.addDirectoryItems(self.handle, listing, len(listing))
        # Add a sort method for the virtual folder items
        xbmcplugin.addSortMethod(self.handle, xbmcplugin.SORT_METHOD_LABEL)
        xbmcplugin.endOfDirectory(self.handle)

    def list_programs(self):
        """
        Create the list of video programs in the Kodi interface.
        """
        programs = get_programs()
        listing = []
        for program in programs:
            title = program.get('title')
            program_url = program.get('@id')
            # Create a list item with a text label and a thumbnail image.
            list_item = xbmcgui.ListItem(label=title)
            list_item.setInfo('video', {'title': title, 'mediatype': 'tvshow'})
            url = '{0}?action=videolisting&program={1}'.format(
                self.url, program_url)
            is_folder = True
            listing.append((url, list_item, is_folder))

        # Set Content
        xbmcplugin.setContent(self.handle, 'tvshows')
        # Add our listing to Kodi.
        xbmcplugin.addDirectoryItems(self.handle, listing, len(listing))
        # Add a sort method for the virtual folder items
        xbmcplugin.addSortMethod(self.handle, xbmcplugin.SORT_METHOD_NONE)
        xbmcplugin.endOfDirectory(self.handle)

    def list_last_broadcast(self):
        """
        Create the list of video programs in the Kodi interface.
        """
        import sys
        items = xbmcplugin.getSetting(int(sys.argv[1]), 'broadcast_items')
        # items = xbmcplugin.getSetting(int(sys.argv[1]), "broadcast_items")
        last_broadcast = get_last_broadcast(items)
        listing = []
        for episode in last_broadcast:
            title = episode.get('title')
            date = episode.get('broadcast_date', '')
            try:
                date = date.split('T')[0]
                title = u'{} ({})'.format(episode.get('title'), date)
            except:
                title = episode.get('title')

            desc = episode.get('description')
            episode_url = episode.get('@id')
            # Create a list item with a text label and a thumbnail image.
            list_item = xbmcgui.ListItem(label=title)
            # Set graphics (thumbnail, fanart, banner, poster, landscape etc.) for the list item.
            list_item.setArt({'thumb': episode.get('episode_image_thumbnail'),
                              'fanart': episode.get('episode_image')})

            list_item.setInfo('video', {'title': title, 'plot': desc, 'mediatype': 'episode'})
            url = '{0}?action=videoepisode&program={1}'.format(self.url, episode_url)
            is_folder = True
            listing.append((url, list_item, is_folder))

        # Set Content
        xbmcplugin.setContent(self.handle, 'episodes')
        # Add our listing to Kodi.
        xbmcplugin.addDirectoryItems(self.handle, listing, len(listing))
        # Add a sort method for the virtual folder items
        xbmcplugin.addSortMethod(self.handle, xbmcplugin.SORT_METHOD_NONE)
        xbmcplugin.endOfDirectory(self.handle)

    def list_programs_types(self):
        """
        Create the list of video programs in the Kodi interface.
        """
        programs_types = get_programs_types()
        listing = []
        for program in programs_types:
            title = program.get('title')
            program_url = program.get('@id')
            # Create a list item with a text label and a thumbnail image.
            list_item = xbmcgui.ListItem(label=title)
            list_item.setInfo('video', {'title': title, 'mediatype': 'tvshow'})
            url = '{0}?action=videotypelisting&program={1}'.format(self.url, program_url)
            is_folder = True
            listing.append((url, list_item, is_folder))

        # Set Content
        xbmcplugin.setContent(self.handle, 'tvshows')
        # Add our listing to Kodi.
        xbmcplugin.addDirectoryItems(self.handle, listing, len(listing))
        # Add a sort method for the virtual folder items
        xbmcplugin.addSortMethod(self.handle, xbmcplugin.SORT_METHOD_NONE)
        xbmcplugin.endOfDirectory(self.handle)

    def list_programs_types_playlist(self, url):
        """
        Create the list of video programs in the Kodi interface.
        """
        programs_types = get_programs_types_playlist(url)
        # xbmc.log(str(programs_types))
        listing = []
        for program in programs_types:
            title = program.get('title')
            program_url = program.get('@id')
            # Create a list item with a text label and a thumbnail image.
            list_item = xbmcgui.ListItem(label=title)
            list_item.setInfo('video', {'title': title, 'mediatype': 'tvshow'})
            url = '{0}?action=videolisting&program={1}'.format(self.url, program_url)
            is_folder = True
            listing.append((url, list_item, is_folder))

        # Set Content
        xbmcplugin.setContent(self.handle, 'tvshows')
        # Add our listing to Kodi.
        xbmcplugin.addDirectoryItems(self.handle, listing, len(listing))
        # Add a sort method for the virtual folder items
        xbmcplugin.addSortMethod(self.handle, xbmcplugin.SORT_METHOD_NONE)
        xbmcplugin.endOfDirectory(self.handle)

    def list_episodes(self, url):
        """
        Create the list of episodes for a given program
        """
        listing = []
        episodes = get_episodes(url)
        for episode in episodes:
            title = episode.get('title')
            date = episode.get('broadcast_date', '')
            try:
                date = date.split('T')[0]
                title = u'{} ({})'.format(episode.get('title'), date)
            except:
                title = episode.get('title')

            desc = episode.get('description')
            episode_url = episode.get('@id')
            # Create a list item with a text label and a thumbnail image.
            list_item = xbmcgui.ListItem(label=title)
            # Set graphics (thumbnail, fanart, banner, poster, landscape etc.) for the list item.
            list_item.setArt({'thumb': episode.get('episode_image_thumbnail'),
                              'fanart': episode.get('episode_image')})

            list_item.setInfo('video', {'title': title, 'plot': desc, 'mediatype': 'episode'})
            url = '{0}?action=videoepisode&program={1}'.format(self.url, episode_url)
            is_folder = True
            listing.append((url, list_item, is_folder))

        # Set Content
        xbmcplugin.setContent(self.handle, 'episodes')
        # Add our listing to Kodi.
        xbmcplugin.addDirectoryItems(self.handle, listing, len(listing))
        # Add a sort method for the virtual folder items
        xbmcplugin.addSortMethod(self.handle, xbmcplugin.SORT_METHOD_NONE)
        xbmcplugin.endOfDirectory(self.handle)

    def list_videos(self, url):
        """
        Create the list of playable videos in the Kodi interface.
        """
        videos = get_videos(url)
        listing = []
        for video in videos.get('formats'):
            if video.get('ext') == 'mp4':
                title = u'{0} ({1})'.format(video['format'], videos['title'])
                # Create a list item with a text label and a thumbnail image.
                list_item = xbmcgui.ListItem(label=title)
                # Set additional info for the list item.
                list_item.setInfo('video', {'title': title, 'mediatype': 'video'})
                # Set graphics (thumbnail, fanart, banner, poster, landscape etc.) for the list item.
                list_item.setArt({'thumb': videos['thumbnail'], 'icon': videos['thumbnail'], 'fanart': videos['thumbnail']})
                list_item.setProperty('IsPlayable', 'true')
                url = '{0}?action=videoplay&video={1}'.format(self.url, video['url'])
                is_folder = False
                listing.append((url, list_item, is_folder))

        # Set Content
        xbmcplugin.setContent(self.handle, 'episodes')
        # Add our listing to Kodi.
        xbmcplugin.addDirectoryItems(self.handle, listing, len(listing))
        # Add a sort method for the virtual folder items
        xbmcplugin.addSortMethod(self.handle, xbmcplugin.SORT_METHOD_NONE)
        xbmcplugin.endOfDirectory(self.handle)

    def play_video(self, path):
        """
        Play a video by the provided path.
        """
        play_item = xbmcgui.ListItem(path=path)
        # Pass the item to the Kodi player.
        xbmcplugin.setResolvedUrl(self.handle, True, listitem=play_item)
