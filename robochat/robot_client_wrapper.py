from abc import abstractmethod,ABCMeta
        
class RobotClientWrapper(metaclass=ABCMeta):
    def __init__(self) -> None:
        pass
    
    def __repr__(self):
        return f"Robot client wrapper {id(self)}"


    @abstractmethod
    def moveto(self,pose:list)->None:
        """ 
        Move to position in blocking mode.
        This method should be overridden.
        """
        pass

    @abstractmethod
    def turn(self,angle:float)->None:
        """
        Turn relatively in blocking mode.
        This method should be overridden.
        """
        pass

    @abstractmethod
    def get_point_pose(self,point_name:str)->list:
        """
        Get the position of a point in blocking mode.
        This method should be overridden.
        Return None if the point is not found.
        """
        return None

    @abstractmethod
    def current_pose(self)->list:
        """
        Return robot current position.
        A valid position should be like [x,y,theta].
        """
        return None
    
    @abstractmethod
    def stop(self)->None:
        """
        Stop all robot actions at once.
        """
        pass
    
    