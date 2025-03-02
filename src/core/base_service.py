from fastapi import HTTPException
import logging
from typing import Callable, Any

class BaseService:
    """Clase base para manejo centralizado de excepciones en servicios"""

    def execute(self, func: Callable[..., Any], *args, **kwargs) -> Any:
        try:
            result = func(*args, **kwargs)
            if result is None:
                raise HTTPException(status_code=404, detail="Recurso no encontrado")
            return result
        except HTTPException:  
            raise  
        except ValueError as e:
            logging.warning(f"Error de validación en {func.__name__}: {str(e)}")
            raise HTTPException(status_code=400, detail=f"Error de validación: {str(e)}")
        except KeyError as e:
            logging.warning(f"Clave no encontrada en {func.__name__}: {str(e)}")
            raise HTTPException(status_code=404, detail=f"Clave no encontrada: {str(e)}")
        except Exception as e:
            logging.error(f"Error inesperado en {func.__name__}: {str(e)}")
            raise HTTPException(status_code=500, detail="Error interno del servidor")
